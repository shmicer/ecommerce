from django.shortcuts import render
from elasticsearch_dsl import Q

from core.documents import ProductDocument
from core.models import Product


def search(request):
    query = request.GET.get('q')
    q = Q(
        'multi_match',
        query=query,
        fields=[
            'name',
            'description',
        ],
        fuzziness='auto')
    products = ProductDocument.search().query(q)
    return render(request, 'search.html', {'products': products})


# def search(request):
#     q = request.GET['q']
#     products = Product.objects.filter(name__icontains=q)
#     return render(request, 'search.html', {'products':products})