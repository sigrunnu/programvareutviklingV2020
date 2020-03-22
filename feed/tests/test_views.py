import pytest
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from mixer.backend.django import mixer


# Overrides WhiteNoise module which throws errors when testing
@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'
)
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.feed_url = reverse('feedHome')
        self.exercise1 = mixer.blend('feed.exercise',
                                     exerciseTitle='exercise1')
        self.exercise_view = reverse('exerciseView', args=[self.exercise1.pk])
        self.create_exercise_view = reverse('addExercise')

    @pytest.mark.filterwarnings('ignore:test_project_home_get')
    def test_feed_home_get(self):
        response = self.client.get(self.feed_url)
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'feed/feed.html')

    def test_exercise_view_get(self):
        response = self.client.get(self.exercise_view)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/exercise_view.html')

    def test_exercise_create_view(self):
        response = self.client.get(self.create_exercise_view)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/exercise_form.html')
