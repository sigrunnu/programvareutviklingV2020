from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import MuscleGroup, Favorisation, Rating, Exercise


class ExerciseAdmin(ImageCroppingMixin, admin.ModelAdmin):
    filter_horizontal = ('muscle_group',)
    list_display = (
        "exercise_title",
        "pub_date",
        "rating_score",
        "number_of_favorisations",
        "is_public",
        "created_by"
    )

    @staticmethod
    def rating_score(obj):
        return obj.get_rating_score()

    @staticmethod
    def number_of_favorisations(obj):
        return obj.get_number_of_favorisations()

    admin.site.register(MuscleGroup)


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Favorisation)
admin.site.register(Rating)
