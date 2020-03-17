from django.test import SimpleTestCase
from django.urls import reverse, resolve

from feed.views import home, exercise_view, ExerciseCreateView, search


class TestUrls(SimpleTestCase):

    def test_feedHome_is_resolved(self):
        url = reverse('feedHome')
        self.assertEqual(resolve(url).func, home)

    def test_exercise_view_is_resolved(self):
        url = reverse('exerciseView', args=['1'])
        self.assertEqual(resolve(url).func, exercise_view)

    def test_ExerciseCreateView_is_resolved(self):
        url = reverse('addExercise')
        self.assertEqual(resolve(url).func.view_class, ExerciseCreateView)

    def test_search_is_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)
