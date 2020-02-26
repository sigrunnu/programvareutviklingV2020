import json
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from search_indexes.documents.exercise import ExerciseDocument


class ExerciseDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""
    id = serializers.IntegerField(read_only=True)
    exerciseTitle = serializers.CharField(read_only=True)
    exerciseInfo = serializers.CharField(read_only=True)

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = ExerciseDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'exerciseTitle',
            'pub_date',
            'createdByPro',
            'exerciseHowTo',
            'exerciseImage',
            'exerciseInfo',
            'exerciseLikes',
            'exerciseRating',
            'exerciseAuthor'
        )
