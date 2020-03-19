import sys

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from feed.models import Exercise, Favorisation
from django.contrib import auth

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
        if str(exercise.createdBy) == user.username:
            published_exercises.append(exercise)

    context = {
        'publishedExercises': published_exercises,
        'favourites': favorised_exercises,
    }

    return render(request, 'profile_page/profile_view.html', context)


def signupView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form': form})


def LoginView(request):
    return render(request, "registration/login.html")
