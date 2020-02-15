import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:
    def test_exercise_title_not_empty(self):
        exercise = mixer.blend('feed.Exercise', exerciseTitle="Bench press")
        assert len(exercise.exerciseTitle) > 0

