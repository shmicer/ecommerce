from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from .models import Product, Category, Manufacturer
# from cart.forms import CartAddProductForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Product.objects.filter(is_featured=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class CategoryView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_list.html'

class BrandView(ListView):
    model = Manufacturer
    context_object_name = 'brands'
    template_name = 'brand_list.html'


class ProductView(ListView):
    model = Product
    context_object_name = 'items'
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = context['items'].distinct().values('category__name', 'category__id')
        # context['brands'] = context['items'].distinct().values('manufacturer__name', 'manufacturer__id')
        return context

def search(request):
    q = request.GET['q']
    products = Product.objects.filter(name__icontains=q)
    return render(request, 'search.html', {'products':products})

def filter_data(request):
    cats = request.GET.getlist('category[]')
    # brands = request.GET.getlist('manufacturer[]')
    all_products = Product.objects.all()
    if len(cats) > 0:
        all_products = all_products.filter(category_id__in=cats).distinct()
    # if len(brands) > 0:
    #     all_products = all_products.filter(manufacturer__id__in=brands).distinct()
    t=render_to_string('ajax/product-list.html', {'items': all_products})
    return JsonResponse({'items': t})