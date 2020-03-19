from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from feed.views import ExerciseCreateView
from . import views

urlpatterns = [
    # Maps to home view in views.py

    path('', views.home, name='feedHome'),
    path('search/', views.search, name='search'),
    path('<int:exercise_id>', views.exercise_view, name='exerciseView'),
    path('addExercise', ExerciseCreateView.as_view(), name="addExercise"),
    path('favoriseExercise/<int:exercise_id>', views.favorise,
         name='favoriseExercise')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
