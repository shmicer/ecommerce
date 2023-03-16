from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category, Manufacturer
from cart.forms import CartAddProductForm


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


def checkout(request):
    return render(request, 'create.html')


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
        context['cats'] = context['items'].distinct().values('category__name')
        context['brands'] = context['items'].distinct().values('manufacturer__name')
        return context
