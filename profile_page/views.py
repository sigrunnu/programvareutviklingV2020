import sys
from feed.models import Exercise, Favorisation
from django.contrib import auth
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
sys.path.append('/64/feed/models')


@login_required
def profile(request):
    user = auth.get_user(request)

    favorised_exercises = []
    for f in Favorisation.objects.all():
        if f.user.id == user.id:
            favorised_exercises.append(f.exercise)

    published_exercises = []
    for exercise in Exercise.objects.all():
        if str(exercise.created_by) == user.username:
            published_exercises.append(exercise)

    context = {
        'publishedExercises': published_exercises,
        'favourites': favorised_exercises,
    }

    return render(request, 'profile_page/profile_view.html', context)


def signupView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.profile.is_pro = form.cleaned_data.get('is_pro')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {'form': form})


def LoginView(request):
    return render(request, "registration/login.html")
