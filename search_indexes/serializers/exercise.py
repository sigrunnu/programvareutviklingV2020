from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from search_indexes.documents.exercise import ExerciseDocument


class ExerciseDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""
    id = serializers.IntegerField(read_only=True)
    exercise_title = serializers.CharField(read_only=True)
    exercise_info = serializers.CharField(read_only=True)

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = ExerciseDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'exercise_title',
            'pub_date',
            'exercise_how_to',
            'exercise_image',
            'exercise_info',
            'created_by',
            'exercise_likes',
            'exercise_rating',

        )
