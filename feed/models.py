from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.db import models
from django.db.models import Q, SET_NULL, Avg
from six import python_2_unicode_compatible
from profile_page.models import CreatedBy, Profile


@python_2_unicode_compatible
class MuscleGroup(models.Model):
    muscle_group_title = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.muscle_group_title

    @staticmethod
    def get_search_vector():
        return (
            SearchVector('muscle_group_title', weight='B')
        )

    @staticmethod
    def get_queryset_by_search_word(search_word):
        """
        :param search_word: the word that shall be searched
        :type search_word: String
        :return: All the objects that contains the search word in
        muscleGroupTitle
        :rtype: QuerySet
        """
        return MuscleGroup.objects.filter(
            Q(muscle_group_title__icontains=search_word))


@python_2_unicode_compatible
class Exercise(models.Model):
    exercise_title = models.CharField(
        max_length=200,
        verbose_name='Tittel på øvelsen'
    )

    exercise_info = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Informasjon om øvelsen'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    favorisations = models.ManyToManyField(
        User,
        through='Favorisation',
        blank=True,
        verbose_name='Favoriseringer',
        related_name='favorisations'
    )
    ratings = models.ManyToManyField(
        User,
        through='Rating',
        blank=True,
        verbose_name='Rangering',
        related_name='ratings'
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name='Offentlig for ikke registrerte brukere'
    )
    exercise_how_to = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Utførelse av øvelsen'
    )
    exercise_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='exercises/',
        verbose_name='Bilde av øvelsen'
    )

    muscle_group = models.ManyToManyField(
        MuscleGroup,
        blank=True,
        verbose_name='Muskelgrupper'
    )
    created_by = models.ForeignKey(
        CreatedBy,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        verbose_name='Laget av'
    )

    class Meta(object):
        ordering = ["exercise_title"]

    def __str__(self):
        return self.exercise_title

    def get_number_of_favorisations(self):
        return len(Favorisation.objects.filter(
            exercise__id=self.id
        ))

    def get_rating_score(self):
        ratings = [r.rating_number for r in Rating.objects.filter(
            exercise__id=self.id
        )]
        if len(ratings) == 0:
            return 0
        average = sum(ratings) / len(ratings)
        return round(average, 1)

    @property
    def muscle_group_indexing(self):
        """Muscle group for indexing. Used in Elasticsearch indexing.
            We only need a flat list of MuscleGroups titles, on which
            we can filter. Therefore, we define a properly on a model level,
            which will return a JSON dumped list of MuscleGroups relevant to
            the current Exercise model object.
        """
        return [
            muscle_group.muscle_group_title
            for muscle_group in self.muscle_group.all()
        ]

    @staticmethod
    def get_search_vector():
        return (
            SearchVector('exercise_title', weight='A', config='norwegian')
        )

    @staticmethod
    def get_queryset_by_search_word(search_word):
        """
        :param search_word: the word that shall be searched
        :type search_word: String
        :return: All the objects that contains the search word in
        exerciseTitle or exerciseDescription
        :rtype: QuerySet
        """
        return Exercise.objects.filter(
            Q(exerciseInfo__icontains=search_word)
            | Q(exerciseTitle__icontains=search_word))


class Favorisation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_in_favorisation'
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='exercise_in_favorisation')

    def __str__(self):
        return self.user.username + " for " + self.exercise.exercise_title


class Rating(models.Model):
    VERY_LOW = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    VERY_HIGH = 5
    RATING_CHOICES = (
        (VERY_LOW, 'Very low'),
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
        (VERY_HIGH, 'Very high'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_in_rating',
        limit_choices_to=Q(profile__is_pro=True)
    )

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='exercise_in_rating'
    )
    rating_number = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.user.username + " for " + self.exercise.exercise_title
