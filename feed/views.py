from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from elasticsearch_dsl import Q
from search_indexes.documents.exercise import ExerciseDocument
from .models import Exercise
from profile_page.models import CreatedBy
from feed.models import Exercise, Favorisation, User, Rating
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
            if exercise.is_public:
                latest_exercises.append(exercise)
    else:
        latest_exercises = Exercise.objects.all()

    print(latest_exercises[0].get_number_of_favorisations())

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
        exercise_title={'value': f'*{search_content}*'}
    )
    q2 = Q(
        "wildcard",
        muscle_group_title={'value': f'*{search_content}*'}
    )

    q3 = q1 | q2
    query = ExerciseDocument.search().query(q3)
    result = query.execute()
    exercises = []
    print(result['hits']['hits'])
    for exercise in result['hits']['hits']:
        try:
            exercises.append(
                Exercise.objects.filter(
                    pk=int(exercise['_source']['id'])).values()[0]
            )
        except IndexError as e:
            print(e)
            pass

    user = auth.get_user(request)
    # Determines if the user is not logged in
    if str(user) == "AnonymousUser":
        for i in range(len(exercises)):
            print(exercises[i])
            if not exercises[i]["is_public"]:
                try:
                    exercises.remove(i)
                except ValueError as e:
                    print(e)
                    pass
    if search_content == '':
        exercises = Exercise.objects.all()

    context = {
        'exercises': exercises
    }
    return render(request, 'feed/feed.html', context)


def favorise(request, exercise_id):
    user = auth.get_user(request)

    exercise_is_liked_by = []

    for favourite in Favorisation.objects.all():
        if favourite.exercise.id == exercise_id:
            exercise_is_liked_by.append(favourite.user_id)

    if user.id not in exercise_is_liked_by:
        favourisation = Favorisation(
            user=user,
            exercise=get_object_or_404(Exercise, pk=exercise_id))

        Favorisation.save(favourisation)

    return exercise_view(request, exercise_id)


def rate_exercise(request, exercise_id):
    user = auth.get_user(request)

    exercise_is_rated_by = []

    for rating in Rating.objects.all():
        if rating.exercise.id == exercise_id:
            exercise_is_rated_by.append(rating.user_id)

    if user.id not in exercise_is_rated_by:
        rating = Rating(
            user=user,
            exercise=get_object_or_404(Exercise, pk=exercise_id),
            rating_number=request.GET['rating_field']
        )
        Rating.save(rating)
        rating_message = 'Ratingen er lagret'
    else:
        rating_message = 'Du har allerede ratet denne øvelsen'
    return exercise_view(
        request,
        exercise_id,
        rating_message=rating_message
    )


def exercise_view(request, exercise_id, **kwargs):
    """
    :param request:
    :type request:
    :param exercise_id: Primary key for Exercise object
    :type exercise_id: Integer
    :return: response with Exercise object that has exercise_id as primary key
    :rtype: HttpResponse
    """

    exercise = get_object_or_404(Exercise, pk=exercise_id)
    favouirites = exercise.get_number_of_favorisations()
    rating_score = exercise.get_rating_score()
    user = auth.get_user(request)

    context = {}

    try:
        rating_message = kwargs['rating_message']
    except KeyError:
        rating_message = ''

    # Determines if the user is not logged in and exercise is hidden
    if str(user) == "AnonymousUser":

        if not exercise.is_public:
            context = {
                'exercise': exercise,
                'favouirites': favouirites,
                'rating_score': rating_score
            }

        else:
            context = {
                'exercise': exercise,
                'favouirites': favouirites,
                'rating_score': rating_score,
                'can_see': True
            }

    else:
        context = {
            'exercise': exercise,
            'favouirites': favouirites,
            'rating_score': rating_score,
            'rating_message': rating_message,
            'can_see': True
        }

    return render(request, 'feed/exercise_view.html', context)


class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'feed/exercise_form.html'
    success_url = '/'
    fields = (
        'exercise_title', 'exercise_info', 'exercise_how_to', 'is_public',
        'exercise_image', 'muscle_group')

    def form_valid(self, form):
        model = form.save(commit=False)
        if self.request.user.is_authenticated:
            model.created_by = CreatedBy.objects.get(user=self.request.user)
        else:
            model.is_public = True
        model.save()
        return HttpResponseRedirect(self.success_url)
