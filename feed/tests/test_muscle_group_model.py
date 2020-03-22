import pytest
import unittest
from mixer.backend.django import mixer
from django.db.utils import DataError


@pytest.mark.django_db
class TestModels:

    def test_muscle_group_title_not_empty(self):
        muscle_group = mixer.blend(
            'feed.MuscleGroup',
            muscle_group_title="Biceps"
        )
        assert len(muscle_group.muscle_group_title) > 0

    def test_muscle_group_title_is_correct(self):
        title = "Biceps"
        muscle_group = mixer.blend(
            'feed.MuscleGroup',
            muscle_group_title=title
        )
        assert title == muscle_group.muscle_group_title

    @unittest.expectedFailure
    def test_muscle_group_long_name(self):
        try:
            muscle_group = mixer.blend(
                'feed.MuscleGroup',
                muscle_group_title="Lorem Ipsum is simply dummy text of "
                                   "the printing and typesetting industry. "
                                   "Lorem Ipsum has been the industry's "
                                   "standard dummy text ever since the "
                                   "1500s, when " "an unknown "
                                   "printer took a galley of type "
                                   "and scrambled it to make a type "
                                   "specimen book. It has "
                                   "survived not only five centuries, "
                                   "but also the leap into "
                                   "electronic " "typesetting, remaining "
                                   "essentially unchanged. " "It was"
                                   "popularised in the 1960s with "
                                   "the release "
                                   "of " "Letraset sheets"
                                   "containing Lorem Ipsum passages, and "
                                   "more recently with desktop"
                                   "publishing software like " "Aldus "
                                   "PageMaker"
                                   " including versions of"
                                   "Lorem Ipsum." "the printing "
                                   "and typesetting "
                                   "industry. " "Lorem Ipsum"
                                   "has been the industry's standard "
                                   "dummy"
                                   " text ever since the 1500s,"
                                   "when an unknown " "printer took a"
                                   " galley of"
                                   " type and scrambled it to "
                                   "make a type specimen book. It has "
                                   "survived "
                                   "not only " "five"
                                   "centuries, but also the leap into "
                                   "electronic"
                                   "typesetting, remaining"
                                   "essentially unchanged. " "It was "
                                   "popularised"
                                   "in the 1960s with the"
                                   "release of " "Letraset sheets "
                                   "containing "
                                   "Lorem Ipsum passages,"
                                   "and " "more recently with desktop "
                                   "publishing software like " "Aldus"
                                   "PageMaker including versions of"
                                   " Lorem Ipsum.")
        except DataError as err:
            # rollback the previous transaction before starting another
            pass
