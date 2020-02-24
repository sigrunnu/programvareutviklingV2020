from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import Exercise, MuscleGroup
from functools import reduce
from search_indexes.documents.book import BookDocument
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

    client = Elasticsearch()

    s = Search(using=client)

    q = Q("multi_match", query='database', fields=['title'])
    # s = s.query(q)
    #print(s)
    #for x in s:
    #    print(x.title)

    s = s.sort()
    
    for x in s:
        print(x.title)
    result = s
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
