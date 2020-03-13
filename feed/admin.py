from django.contrib import admin

from .models import Exercise
from .models import MuscleGroup
from image_cropping import ImageCroppingMixin


class ExerciseAdmin(ImageCroppingMixin,
                    admin.ModelAdmin):
    pass
    filter_horizontal = ('muscleGroup',)
    admin.site.register(MuscleGroup)


admin.site.register(Exercise, ExerciseAdmin)


