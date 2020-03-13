from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

import profile_page.views

urlpatterns = [
    path('', profile_page.views.profile, name='profile'),
    path('signup/', profile_page.views.signupView, name='signup'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

]
