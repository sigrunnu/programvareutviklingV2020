from unittest import TestCase

import pytest
from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl.documents import DocType
from django_elasticsearch_dsl.exceptions import (ModelFieldNotMappedError,
                                                 RedeclaredFieldError)
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer

from feed.models import Exercise
from search_indexes.documents.exercise import ExerciseDocument


@pytest.mark.django_db
class TestExerciseDocument(TestCase):

    def test_model_class_added(self):
        self.assertEqual(ExerciseDocument.django.model, Exercise)

    def test_ignore_signal_default(self):
        self.assertFalse(ExerciseDocument.django.ignore_signals)

    def test_auto_refresh_default(self):
        self.assertTrue(ExerciseDocument.django.auto_refresh)

    def test_ignore_signal_added(self):
        @registry.register_document
        class ExerciseDocument2(DocType):
            class Django:
                model = Exercise
                ignore_signals = True

        self.assertTrue(ExerciseDocument2.django.ignore_signals)

    def test_auto_refresh_added(self):
        @registry.register_document
        class ExerciseDocument2(DocType):
            class Django:
                model = Exercise
                auto_refresh = False

        self.assertFalse(ExerciseDocument2.django.auto_refresh)

    def test_queryset_pagination_added(self):
        @registry.register_document
        class ExerciseDocument2(DocType):
            class Django:
                model = Exercise
                queryset_pagination = 120

        self.assertIsNone(ExerciseDocument.django.queryset_pagination)
        self.assertEqual(ExerciseDocument2.django.queryset_pagination, 120)

    def test_fields_populated(self):
        mapping = ExerciseDocument._doc_type.mapping
        self.assertEqual(
            set(mapping.properties.properties.to_dict().keys()),
            {'id', 'exercise_title', 'muscle_group_title'}
        )

    def test_duplicate_field_names_not_allowed(self):
        with self.assertRaises(RedeclaredFieldError):
            html_strip = analyzer(
                'html_strip',
                tokenizer="standard",
                filter=["standard", "lowercase", "stop", "snowball"],
                char_filter=["html_strip"]
            )

            @registry.register_document
            class ExerciseDocument(DocType):
                id = fields.IntegerField(attr='id')

                exercise_title = fields.TextField(
                    attr='exercise_title',
                    analyzer=html_strip,
                    fields={
                        'raw': fields.TextField(analyzer='keyword',
                                                multi=True),
                        'suggest': fields.CompletionField(multi=True),
                    },
                )

                muscle_group_title = fields.TextField(
                    attr='muscle_group_indexing',
                    analyzer=html_strip,
                    fields={
                        'raw': fields.TextField(analyzer='keyword',
                                                multi=True),
                        'suggest': fields.CompletionField(multi=True),
                    },
                    multi=True,
                )

                class Django:
                    fields = ['id', 'exercise_title', 'muscle_group_title']
                    model = Exercise

    def test_to_field(self):
        doc = DocType()
        exercise_title = doc.to_field(
            'exercise_title',
            Exercise._meta.get_field('exercise_title')
        )
        self.assertIsInstance(exercise_title, fields.TextField)
        self.assertEqual(exercise_title._path, ['exercise_title'])
        id_field = doc.to_field(
            'id',
            Exercise._meta.get_field('id')
        )
        self.assertIsInstance(id_field, fields.IntegerField)
        self.assertEqual(id_field._path, ['id'])

    def test_to_field_with_unknown_field(self):
        doc = DocType()
        with self.assertRaises(ModelFieldNotMappedError):
            doc.to_field(
                'muscle_group',
                Exercise._meta.get_field('muscle_group')
            )
