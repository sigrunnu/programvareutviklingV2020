from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import profile_page.views

urlpatterns = [
    path('', profile_page.views.profile, name='profile'),
    path('signup/', profile_page.views.signupView, name='signup'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('edit/', profile_page.views.editProfile, name="editProfile"),
    path('password/', profile_page.views.changePassword, name="changePassword")

]
