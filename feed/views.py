from django.shortcuts import render

from .models import Exercise


# Create your views here.
def home(request):

    latest_exercises = Exercise.objects.all()

    context = {
        'exercises': latest_exercises
    }

    return render(request, 'feed/feed.html', context)


def search(request):
    """
    :param request:
    :type request:
    :return:
    :rtype:
    """
    search_word = request.GET['search_field']
    print(search_word)
    return render(request, 'feed/search.html', {'search_content': search_word})


def exerciseView(request):

    context = {
        'exercise': {
            'name': "Benkpress",
            'author': 'Petter',
            'description': "Benkpress er en ganske kompleks øvelse og det "
                           "kreves mye trening for å få til en bra "
                           "utførelse. Dessverre er det ikke så lett som å "
                           "bare legge seg ned på en benk og løfte stangen "
                           "opp og ned.",
            'verified': "true"
        }

    }

    return render(request, 'feed/exercise_view.html', context)
