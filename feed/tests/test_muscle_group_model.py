import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:
    def test_muscle_group_title_not_empty(self):
        muscleGroup = mixer.blend('feed.MuscleGroup',
                                  muscleGroupTitle="Biceps")
        assert len(muscleGroup.muscleGroupTitle) > 0

    def test_muscle_group_title_is_correct(self):
        title = "Biceps"
        muscleGroup = mixer.blend('feed.MuscleGroup',
                                  muscleGroupTitle=title)
        assert title == muscleGroup.muscleGroupTitle
