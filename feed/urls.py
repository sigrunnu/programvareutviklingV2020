from django.urls import path

from . import views

urlpatterns = [
    # Maps to home view in views.py

    path('', views.home, name='feed-home'),
    path('search', views.search, name='search'),
    path('e', views.exerciseView, name='exerciseView')

]
