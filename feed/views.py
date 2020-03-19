from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from elasticsearch_dsl import Q

from feed.models import Exercise, Favorisation, User
from search_indexes.documents.exercise import ExerciseDocument

from django.contrib import auth


# Create your views here.
def home(request):
    """
   :param request: the request the user sends when requesting the home page
   :type request: WSGIRequest
   :return: render: response with all the exercises listed in a QuerySet
   :rtype: HttpResponse
   """
    latest_exercises = []

    user = auth.get_user(request)

    # Determines if the user is not logged in
    if str(user) == "AnonymousUser":
        for exercise in Exercise.objects.all():
            print(exercise)
            if exercise.isPublic:
                latest_exercises.append(exercise)
    else:
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
    exercises = []
    for exercise in result['hits']['hits']:
        exercises.append(
            Exercise.objects.filter(
                pk=int(exercise['_source']['id'])).values()[0]
        )

    user = auth.get_user(request)

    visibleExercises = []

    # Determines if the user is not logged in
    if str(user) == "AnonymousUser":
        for exercise in exercises:
            print(exercise)
            if exercise["isPublic"]:
                visibleExercises.append(exercise)
    else:
        visibleExercises = Exercise.objects.all()

    # TODO: Make the result index fetch the relevant Exercises from the db
    context = {
        'exercises': visibleExercises
    }
    return render(request, 'feed/feed.html', context)


def favorise(request, exercise_id):
    user = auth.get_user(request)

    exerciseIsLikedBy = []

    for favourite in Favorisation.objects.all():
        if favourite.exercise.id == exercise_id:
            exerciseIsLikedBy.append(favourite.user_id)

    if user.id not in exerciseIsLikedBy:
        favourisation = Favorisation(
            user=user,
            exercise=get_object_or_404(Exercise, pk=exercise_id))

        Favorisation.save(favourisation)

    return exercise_view(request, exercise_id)


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
    favouirites = len(exercise.get_number_of_favorisations())

    user = auth.get_user(request)

    context = {}

    # Determines if the user is not logged in and exercise is hidden
    if str(user) == "AnonymousUser":
        if not exercise.isPublic:
            print("Ikke tilgjengelig")

            context = {
                'exercise': exercise,
                'favouirites': favouirites,
            }

        else:
            print("Kan se")
            context = {
                'exercise': exercise,
                'favouirites': favouirites,
                'can_see': True
            }

    return render(request, 'feed/exercise_view.html', context)


class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'feed/exercise_form.html'
    success_url = '/'
    fields = (
        'exerciseTitle', 'exerciseInfo', 'exerciseHowTo', 'exerciseImage',
        'muscleGroup')
