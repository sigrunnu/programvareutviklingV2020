from django.shortcuts import render

from .models import Exercise

# Create your views here.
def home(request):

    latestExercises = Exercise.objects.all()

    context = {
        'exercises': latestExercises
    }

    return render(request, 'feed/search.html', context)
