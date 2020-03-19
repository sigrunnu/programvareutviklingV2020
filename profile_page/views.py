import sys
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
sys.path.append('/64/feed/models')
from feed.models import Exercise, Favorisation
from django.contrib import auth

@login_required
def profile(request):
    latest_exercises = Exercise.objects.all()

    user = auth.get_user(request)
    favorised_exercises = []
    for f in Favorisation.objects.all():
        if f.user.id == user.id:
            favorised_exercises.append(f.exercise)

    context = {
        'exercises': latest_exercises,
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
