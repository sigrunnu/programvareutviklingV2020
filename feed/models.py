from django.db import models


class Exercise(models.Model):
    exerciseTitle = models.CharField(max_length=200)
    exerciseDescription = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.exerciseTitle


""""
class (models.Model):
    question = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""


class MuscleGroup(models.Model):
    muscleGroupTitle = models.CharField(max_length=200)
