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
            'description': "Lorem ipsum dolor sit amet, consectetur "
                           "adipiscing elit, sed do eiusmod tempor "
                           "incididunt ut labore et dolore magna aliqua. Ut "
                           "enim ad minim veniam, quis nostrud exercitation "
                           "ullamco laboris nisi ut aliquip ex ea commodo "
                           "consequat. Duis aute irure dolor in "
                           "reprehenderit in voluptate velit esse cillum "
                           "dolore eu fugiat nulla pariatur. Excepteur sint "
                           "occaecat cupidatat non proident, sunt in culpa "
                           "qui officia deserunt mollit anim id est laborum. ",
            'verified': "VERIFIED"
        }

    }

    return render(request, 'feed/exercise_view.html', context)
