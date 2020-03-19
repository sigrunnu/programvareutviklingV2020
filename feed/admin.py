from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Exercise
from .models import MuscleGroup


class ExerciseAdmin(ImageCroppingMixin,
                    admin.ModelAdmin):
    pass
    filter_horizontal = ('muscleGroup',)
    admin.site.register(MuscleGroup)


admin.site.register(Exercise, ExerciseAdmin)


