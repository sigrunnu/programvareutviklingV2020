from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from books.models.book import Book

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
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    title = fields.TextField(
        attr='title',
        fields={
            'suggest': fields.Completion(),
        }
    )

    class Django(object):
        """Inner nested class Django."""

        model = Book  # The model associate with this Document