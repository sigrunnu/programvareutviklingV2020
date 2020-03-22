from django.shortcuts import get_object_or_404
from django.http import (
    Http404
)
from feed.models import Exercise


def counting_sort_exercises_based_on_rating(exercises):
    """
    This function uses counting sort to sort the incoming exercises based on
    the rating score. Counting sort is a good choice because it sorts in
    linear time and the highest possible rating score is known.
    :param exercises: list with exercise object represented as dictionaries
    :return: a list of exercise objects represented as dictionaries sorted
    by rating score. The higher the rating score, the lower the index in
    the result list
    """
    try:
        highest_value = 50
        exercise_result_list = [0 for i in range(len(exercises))]
        c = [0 for i in range(highest_value+1)]
        for j in range(len(exercises)):
            rating_score = get_object_or_404(
                Exercise,
                pk=exercises[j]['id']
            ).get_rating_score()
            c[int(rating_score * 10)] = c[int(rating_score * 10)] + 1
        for i in range(1, highest_value+1):
            c[i] = c[i] + c[i-1]
        for j in range(len(exercises)-1, -1, -1):
            rating_score = get_object_or_404(
                Exercise,
                pk=exercises[j]['id']
            ).get_rating_score()
            exercise_result_list[c[int(rating_score * 10)]-1] = exercises[j]
            c[int(rating_score * 10)] -= 1
        return reversed(exercise_result_list)
    except ValueError as e:
        print("counting sort got an error, sorting failed: " + str(e))
        return exercises
    except Http404 as e:
        print("counting sort got an error, sorting failed: " + str(e))
        return exercises
