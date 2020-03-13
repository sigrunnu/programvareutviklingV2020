from django.urls import path

import profile_page.views

urlpatterns = [
    path('', profile_page.views.profile, name='profile')

]
