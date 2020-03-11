from datetime import datetime

from django.contrib.postgres.search import SearchVector
from django.db import models
from django.db.models import Q
from six import python_2_unicode_compatible
import profile_page.models.User


@python_2_unicode_compatible
class MuscleGroup(models.Model):
    muscleGroupTitle = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.muscleGroupTitle

    @staticmethod
    def get_search_vector():
        return (
            SearchVector('muscleGroupTitle', weight='B')
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
            Q(muscleGroupTitle__icontains=search_word))


@python_2_unicode_compatible
class Exercise(models.Model):
    exerciseTitle = models.CharField(
        max_length=200,
        verbose_name='Tittel på øvelsen'
    )
    exerciseAuthor = models.CharField(
        max_length=50,
        verbose_name='Forfatternavn',
        null=True
    )
    exerciseInfo = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Informasjon om øvelsen'
    )
    pub_date = models.DateTimeField(
        default=datetime.now(),
        editable=False,
    )
    exerciseLikes = models.IntegerField(
        default=0
    )
    exerciseRating = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=3,
        max_digits=4
    )
    exerciseHowTo = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Utførelse av øvelsen'
    )
    createdByPro = models.BooleanField(
        default=False,
        verbose_name='Profesjonell'
    )
    exerciseImage = models.ImageField(
        null=True,
        blank=True,
        upload_to='exercises/',
        verbose_name='Bilde av øvelsen'
    )
    muscleGroup = models.ManyToManyField(
        MuscleGroup,
        blank=True,
        verbose_name='Muskelgrupper'
    )
    createdBy = models.ForeignKey(
        User,
        verbose_name='Bruker'
    )

    class Meta(object):
        ordering = ["exerciseLikes", "exerciseRating", "exerciseTitle"]

    def __str__(self):
        return self.exerciseTitle

    @property
    def muscle_group_indexing(self):
        """Muscle group for indexing. Used in Elasticsearch indexing.
            We only need a flat list of MuscleGroups titles, on which
            we can filter. Therefore, we define a properly on a model level,
            which will return a JSON dumped list of MuscleGroups relevant to
            the current Exercise model object.
        """
        return [
            muscleGroup.muscleGroupTitle
            for muscleGroup in self.muscleGroup.all()
        ]

    @staticmethod
    def get_search_vector():
        return (
            SearchVector('exerciseTitle', weight='A', config='norwegian')
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
