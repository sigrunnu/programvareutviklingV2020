from django.test import SimpleTestCase
from django.urls import reverse, resolve

from profile_page.views import profile, signupView, LoginView


class TestUrls(SimpleTestCase):

    def test_profile_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_signupView_is_resolved(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signupView)
