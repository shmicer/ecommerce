from django.shortcuts import render
from elasticsearch_dsl import Q

from search.documents import ProductDocument
from core.models import Product


def search(request):
    query = request.GET.get('q')
    q = Q(
        'multi_match',
        query=query,
        fields=[
            'name',
            'description'
        ],
        fuzziness='auto')
    search = ProductDocument.search().query(q)
    products = search.to_queryset()
    return render(request, 'search.html', {'products': products})
