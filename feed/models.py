from django.db import models


class MuscleGroup(models.Model):
    muscleGroupTitle = models.CharField(max_length=200)

    def __str__(self):
        return self.muscleGroupTitle


class Exercise(models.Model):
    exerciseTitle = models.CharField(max_length=200)
    exerciseDescription = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    muscleGroup = models.ManyToManyField(MuscleGroup)

    def __str__(self):
        return self.exerciseTitle
