from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import Exercise, MuscleGroup
from functools import reduce


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

    # Creates list of search words
    search_words = search_content.split(' ')

    # Checks that there was not a space as the last character
    if len(search_words) > 1 and search_words[-1] == '':
        search_words.pop(-1)

    index_list = list(set((i for i in range(len(search_words)))))
    print(index_list)
    ps = []
    for i in range(1, 1 << len(index_list)):
        ps.append([index_list[j] for j in range(len(index_list)) if i & (1 << j)])


    print(ps)
    result = Exercise.objects.none()
    for search in ps:
        search_string = ''
        for index in search:
            search_string += ' ' + search_words[index]
        search_string.strip()
        print(search_string)
        print(result)
        w = Exercise.get_queryset_by_search_word(search_string)
        result = result.union(w)
        print(result)
    # Context stores the search by the keys: exercises, muscleGroups
    print(result)
    context = {
        'exercises': result
    }

    return render(request, 'feed/feed.html', context)


def exercise_view(request, exercise_id):
    """
    :param request:
    :type request:
    :param exercise_id: Primary key for Exercise object
    :type exercise_id: Integer
    :return: response with Exercise object that has exercise_id as primary key
    :rtype: HttpResponse
    """

    exercise = get_object_or_404(Exercise, pk=exercise_id)

    context = {
        'exercise': exercise
    }

    return render(request, 'feed/exercise_view.html', context)
