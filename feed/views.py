from django.contrib import auth
from django.http import (
    Http404
)
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from elasticsearch_dsl import Q

from feed.models import Exercise, Favorisation, Rating
from feed.utils import counting_sort_exercises_based_on_rating
from profile_page.models import CreatedBy
from search_indexes.documents.exercise import ExerciseDocument


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

    latest_exercises = counting_sort_exercises_based_on_rating(
        latest_exercises
    )
    context = {
        'exercises': latest_exercises
    }

    return render(request, 'feed/feed.html', context)


def search(request):
    """
    :param request: the request that contains the search word
    :type request: WSGIRequest
    :return: render: if search content not empty string:
    response with search content. Else: all exercise objects.
    The response list is always sorted based on the professional ranking
    :rtype: HttpResponse with a list of exercise objects
    """

    # search_content fetches the string entered into search_field
    search_content = request.GET['search_field']

    if search_content == '':
        # Just pressing enter in the search field is a shortcut for fetching
        # all the exercises. Thus all the exercise objects are rendered
        exercises = Exercise.objects.all()
    else:
        # Search queries are made for the elastic search.
        # Uses "wildcard" meaning that it searches fro strings that contains
        # the search string. Has two equally weighted queries. One for
        # exercise title and one for muscle group title
        q1 = Q(
            "wildcard",
            exercise_title={'value': f'*{search_content}*'}
        )
        q2 = Q(
            "wildcard",
            muscle_group_title={'value': f'*{search_content}*'}
        )

        # Uses a binary or operation to merge the two queries into one query
        q3 = q1 | q2

        query = ExerciseDocument.search().query(q3)
        result = query.execute()

        # Fetches the relevant exercise objects from the database.
        # This will be the array we pass to the view
        exercises = []
        for exercise in result['hits']['hits']:
            try:
                exercises.append(
                    get_object_or_404(
                        Exercise,
                        pk=int(exercise['_source']['id'])
                    )
                )
            except ValueError as e:
                print(e)
                pass
            except Http404 as e:
                print(e)
                pass
        # Exercises now contains all Exercise objects that matches the search
        # in the order the search returned

    user = auth.get_user(request)
    # Determines if the user is not logged in
    if str(user) == "AnonymousUser":
        for i in range(len(exercises)):
            print(exercises[i])
            if not exercises[i].is_public is True:
                try:
                    # Is the user is not registered and the exercise is
                    # not public. Remove it form the list we are going
                    # to render
                    exercises.remove(i)
                except ValueError as e:
                    print(e)
                    pass

    # Now we have the final list of exercises. We then need to sort it based
    # on the professional rating

    exercises = counting_sort_exercises_based_on_rating(exercises)

    context = {
        'exercises': exercises
    }
    return render(request, 'feed/feed.html', context)


def favorise(request, exercise_id):
    """
    :param request: request sent when the user pressed the favorise button
    :type request: WSGIRequest
    :param exercise_id: the id of the exercise object to be favorised
    :type exercise_id: integer
    :return: request: the same request that was received in the params.
    No modifications are done.
    exercise_id: the same id as was received in the params,
    :rtype: request: WSGIRequest, exercise_id: integer
    """
    user = auth.get_user(request)

    exercise_is_liked_by = []

    for favourite in Favorisation.objects.all():
        if favourite.exercise.id == exercise_id:
            exercise_is_liked_by.append(favourite.user_id)
    # Checks if the user has not already favorised the exercise
    if user.id not in exercise_is_liked_by:
        favorisation = Favorisation(
            user=user,
            exercise=get_object_or_404(Exercise, pk=exercise_id))

        Favorisation.save(favorisation)

    return exercise_view(request, exercise_id)


def rate_exercise(request, exercise_id):
    """
    :param request: request sent when the user pressed the rating button
    :type request: WSGIRequest
    :param exercise_id: the id of the exercise object to be rated
    :type exercise_id: integer
    :return: request: the same request that was received in the params.
    No modifications are done.
    exercise_id: the same id as was received in the params.
    exercise_message: string that represents the status of the rating
    :rtype: request: WSGIRequest, exercise_id: integer,
    exercise_message: string
    """
    user = auth.get_user(request)

    exercise_is_rated_by = []

    for rating in Rating.objects.all():
        if rating.exercise.id == exercise_id:
            exercise_is_rated_by.append(rating.user_id)

    if user.id not in exercise_is_rated_by:
        try:
            rating = Rating(
                user=user,
                exercise=get_object_or_404(Exercise, pk=exercise_id),
                rating_number=request.GET['rating_field']
            )
            Rating.save(rating)
            rating_message = 'Ratingen er lagret'
        except ValueError as e:
            print("An error occurred: " + str(e))
            rating_message = 'Det skjedde en feil'

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
            'can_see': True,
            'logged_in': True
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
