import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:
    def test_exercise_title_not_empty(self):
        exercise = mixer.blend('feed.Exercise', exercise_title="Bench press")
        assert len(exercise.exercise_title) > 0

    def test_description_not_empty(self):
        exercise = mixer.blend('feed.Exercise',
                               exercise_description="Some description")
        assert len(exercise.exercise_description) > 0

    def test_exercise_title_is_correct(self):
        title = "Bicep curl"
        exercise = mixer.blend('feed.Exercise', exercise_title=title)
        assert title == exercise.exercise_title

    def test_description_is_correct(self):
        description = "Some description"
        exercise = mixer.blend('feed.Exercise',
                               exercise_description=description)
        assert description == exercise.exercise_description

    def test_exercise_to_muscle_group_not_empty(self):
        muscle_group = mixer.blend('feed.MuscleGroup')
        exercise = mixer.blend('feed.Exercise', muscle_group=muscle_group)
        assert exercise.muscle_group.count() > 0
