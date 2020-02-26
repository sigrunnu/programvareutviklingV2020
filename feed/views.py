from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from search_indexes.documents.exercise import ExerciseDocument
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import Exercise, MuscleGroup
from functools import reduce
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Q


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

    query = ExerciseDocument.search().query(
        "wildcard",
        exerciseTitle={'value': f'*{search_content}*'}
    )

    result = query.execute()
    print(result.to_dict())
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


class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'feed/exercise_form.html'
    success_url = '/'
    fields = (
        'exerciseTitle', 'exerciseAuthor', 'exerciseInfo', 'exerciseHowTo',
        'createdByPro', 'exerciseImage', 'muscleGroup')
