from django.contrib import admin
from image_cropping import ImageCroppingMixin

from feed.models import Exercise
from feed.models import MuscleGroup, Favorisation


class ExerciseAdmin(ImageCroppingMixin,
                    admin.ModelAdmin):
    pass
    filter_horizontal = ('muscleGroup',)
    admin.site.register(MuscleGroup)


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Favorisation)
