from django.shortcuts import render, get_object_or_404

from .models import Exercise, MuscleGroup


# Create your views here.
def home(request):
    """
   :param request: the request the user sends when requesting the home page
   :type request: WSGIRequest
   :return: render: response with all the exercises listed in a QuerySet
   :rtype: HttpResponse
   """
    latest_exercises = Exercise.objects.all()

    context = {
        'exercises': latest_exercises
    }

    return render(request, 'feed/feed.html', context)


def search(request):
    """
    :param request: the request that contains the search word
    :type request: WSGIRequest
    :return: render: response with search content
    :rtype: HttpResponse
    """

    # search_content fetches the string entered into search_field
    search_content = request.GET['search_field']

    # List of all search words in search_content
    search_words = search_content.split(' ')

    result_exercise = Exercise.objects.none()
    result_muscle_group = MuscleGroup.objects.none()

    # Uses static method in Models to fetch QuerySet with Objects that
    # contains the search word
    for i in range(len(search_words)):
        result_exercise = \
            result_exercise | Exercise.get_queryset_by_search_word(
                search_words[i])
        result_muscle_group = \
            result_muscle_group | \
            MuscleGroup.get_queryset_by_search_word(search_words[i])

    # Context stores the search by the keys: exercises, muscleGroups
    context = {
        'exercises': result_exercise,
        'muscle_groups': result_muscle_group
    }

    return render(request, 'feed/feed.html', context)


def exercise_view(request, exercise_id):
    """
    :param request:
    :type request:
    :param exercise_id:
    :type exercise_id:
    :return:
    :rtype:
    """

    exercise = get_object_or_404(Exercise, pk=exercise_id)

    context = {
        'exercise': exercise
    }

    return render(request, 'feed/exercise_view.html', context)
