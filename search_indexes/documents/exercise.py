from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from feed.models import Exercise

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@INDEX.doc_type
class ExerciseDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    exercise_title = fields.TextField(
        attr='exercise_title',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', multi=True),
            'suggest': fields.CompletionField(multi=True),
        },
    )

    muscle_group_title = fields.TextField(
        attr='muscle_group_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', multi=True),
            'suggest': fields.CompletionField(multi=True),
        },
        multi=True,
    )

    class Django(object):
        """Inner nested class Django."""

        model = Exercise  # The model associate with this Document
