i>mport pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:
    def test_exercise_title_not_empty(self):
        exercise = mixer.blend('feed.Exercise', exerciseTitle="Bench press")
        assert len(exercise.exerciseTitle) > 0

    def test_description_not_empty(self):
        exercise = mixer.blend('feed.Exercise',
                               exerciseDescription="Some description")
        assert len(exercise.exerciseDescription) > 0

    def test_exercise_title_is_correct(self):
        title = "Bicep curl"
        exercise = mixer.blend('feed.Exercise', exerciseTitle=title)
        assert title == exercise.exerciseTitle

    def test_description_is_correct(self):
        description = "Some description"
        exercise = mixer.blend('feed.Exercise',
                               exerciseDescription=description)
        assert description == exercise.exerciseDescription

    def test_exercise_to_musclegroup_not_empty(self):
        muscleGroup = mixer.blend('feed.MuscleGroup')
        exercise = mixer.blend('feed.Exercise', muscleGroup=muscleGroup)
        assert exercise.muscleGroup.count() > 0
