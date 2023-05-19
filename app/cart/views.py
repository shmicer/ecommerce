from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, FormView

from core.models import Product
from django.views import View

from .cart import Cart
from .forms import CartAddProductForm


class CartView(View):

    def get(self, cart):
        cart = Cart(self.request)
        if len(cart) == 0:
            return render(self.request, 'empty-cart.html')
        return render(self.request, 'cart.html')


def add_to_cart(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=item,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('home')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Product, id=product_id)
    cart.remove(item)
    return redirect('cart')


def increase_quantity(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Product, id=product_id)
    cart.increase_quantity(item)
    return redirect('cart')


def decrease_quantity(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Product, id=product_id)
    cart.decrease_quantity(item)
    return redirect('cart')

