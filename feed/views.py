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

    # Search Query
    search_words = search_content.split(' ')
    search_queries = [SearchQuery(search_content), SearchQuery(''.join(search_words))]
    for i in range(len(search_words)):
        if search_words[i] == '':
            search_words.pop(i)
    for search_word in search_words:
        search_queries.append(SearchQuery(search_word))
    super_query = reduce(lambda x, y: x | y, search_queries)
    vector_exercise = Exercise.get_search_vector()
    vector_musclegroup = MuscleGroup.get_search_vector()


    # Context stores the search by the keys: exercises, muscleGroups
    context = {
        'exercises': Exercise.objects.annotate(rank=SearchRank(vector_exercise, super_query, weights=[0.1, 0.2, 0.3, 1])).order_by('-rank'),
        'muscle_groups': MuscleGroup.objects.annotate(rank=SearchRank(vector_musclegroup, super_query)).order_by('-rank')
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
