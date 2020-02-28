from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from elasticsearch_dsl import Q

from search_indexes.documents.exercise import ExerciseDocument
from .models import Exercise


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

    q1 = Q(
        "wildcard",
        exerciseTitle={'value': f'*{search_content}*'}
    )
    q2 = Q(
        "wildcard",
        muscleGroupTitle={'value': f'*{search_content}*'}
    )

    q3 = q1 | q2

    query = ExerciseDocument.search().query(q3)
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
        'createdByPro', 'muscleGroup')
