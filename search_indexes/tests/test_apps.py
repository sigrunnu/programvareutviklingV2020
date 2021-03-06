import pytest
from django.test import TestCase

import search_indexes
from search_indexes.apps import SearchIndexesConfig


@pytest.mark.django_db
class TestApps(TestCase):

    def test_name(self):
        instance = SearchIndexesConfig(
            app_module=search_indexes,
            app_name='search_indexes'
        )
        self.assertEqual(instance.name, 'search_indexes')
