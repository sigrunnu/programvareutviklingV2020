from django.db import models
from django.db.models import Q


class MuscleGroup(models.Model):
    muscleGroupTitle = models.CharField(max_length=200)

    def __str__(self):
        return self.muscleGroupTitle

    @staticmethod
    def get_queryset_by_search_word(search_word):
        """
        :param search_word: the word that shall be searched
        :type search_word: String
        :return: All the objects that contains the search word in muscleGroupTitle
        :rtype: QuerySet
        """
        return MuscleGroup.objects.filter(Q(muscleGroupTitle__icontains=search_word))


class Exercise(models.Model):
    exerciseTitle = models.CharField(max_length=200)
    exerciseDescription = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    muscleGroup = models.ManyToManyField(MuscleGroup, blank=True)

    def __str__(self):
        return self.exerciseTitle

    @staticmethod
    def get_queryset_by_search_word(search_word):
        """
        :param search_word: the word that shall be searched
        :type search_word: String
        :return: All the objects that contains the search word in exerciseTitle or exerciseDescription
        :rtype: QuerySet
        """
        return Exercise.objects.filter(
            Q(exerciseDescription__icontains=search_word)
            | Q(exerciseTitle__icontains=search_word))
