from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Exercise
from .models import MuscleGroup, Favorisation
from profile_page.models import CreatedBy


class ExerciseAdmin(ImageCroppingMixin,
                    admin.ModelAdmin):
    pass

    filter_horizontal = ('muscleGroup',)
    admin.site.register(MuscleGroup)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.createdBy = CreatedBy.objects.get(user=request.user)
            obj.save()


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Favorisation)
