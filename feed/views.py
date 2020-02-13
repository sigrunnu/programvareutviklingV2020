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
    :return: render:
    :rtype: HttpResponse:
    """
    search_word = request.GET['search_field']
    print(search_word)
    return render(request, 'feed/search.html', {'search_content': search_word})
