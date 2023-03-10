from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from cart.forms import CartAddProductForm


class HomeView(ListView):
    model = Product
    context_object_name = 'items'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        context['title'] = 'Sample Store'
        return context

    def get_queryset(self):
        try:
            self.category = Category.objects.get(name=self.kwargs['category'])
            return Product.objects.filter(category__name=self.category)
        except:
            return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


def checkout(request):
    return render(request, 'create.html')