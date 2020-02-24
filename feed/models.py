from django.db import models
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from datetime import datetime
from datetime import datetime
from six import python_2_unicode_compatible


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
        max_length=200
    )
    exerciseAuthor = models.CharField(
        max_length=50
    )
    exerciseInfo = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )
    pub_date = models.DateTimeField(
        default=datetime.now(),
        editable=False
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
        blank=True
    )
    createdByPro = models.BooleanField(default=False)
    exerciseImage = models.ImageField(
        null=True,
        blank=True,
        upload_to='exercises/'
    )
    muscleGroup = models.ManyToManyField(
        MuscleGroup,
        blank=True
    )

    def __str__(self):
        return self.exerciseTitle

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
            Q(exerciseDescription__icontains=search_word)
            | Q(exerciseTitle__icontains=search_word))
