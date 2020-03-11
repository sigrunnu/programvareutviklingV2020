from django.urls import path

from feed.views import ExerciseCreateView
from . import views

urlpatterns = [
    # Maps to home view in views.py

    path('', views.home, name='feedHome'),
    path('search/', views.search, name='search'),
    path('login/', views.loginView, name='loginView'),
    path('signup/', views.signUpView, name='signUpView'),
    path('<int:exercise_id>', views.exercise_view, name='exerciseView'),
    path('addExercise', ExerciseCreateView.as_view(), name="addExercise")

]
