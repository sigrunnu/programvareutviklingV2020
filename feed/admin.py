from django.contrib import admin

from .models import Exercise
from .models import MuscleGroup


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    filter_horizontal = ('muscleGroup',)


admin.site.register(MuscleGroup)
