# django 2.x
from django.urls import reverse
import pytest
from unittest import TestCase
from django.test import TestCase, Client


@pytest.mark.django_db
class TestUrls(TestCase):
    client = Client()

    def test_create(self):
        response = self.client.get('/search/exercises/')
        self.assertEqual(response.status_code, 200)
