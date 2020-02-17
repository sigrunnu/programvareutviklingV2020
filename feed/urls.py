from django.urls import path

from . import views

urlpatterns = [
    # Maps to home view in views.py

    path('', views.home, name='feedHome'),
    path('search', views.search, name='search'),
    path('<int:exercise_id>', views.exercise_view, name='exerciseView')

]

