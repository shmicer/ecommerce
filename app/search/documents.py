from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry

from core.models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {
            "analysis": {
              "analyzer": {
                "my_analyzer": {
                  "tokenizer": "my_tokenizer"
                }
              },
              "tokenizer": {
                "my_tokenizer": {
                  "type": "edge_ngram",
                  "min_gram": 3,
                  "max_gram": 20,
                }
              }
            },
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Product
        fields = [
            'name',
            'description',
        ]

