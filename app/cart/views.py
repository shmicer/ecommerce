from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from core.models import Product
from .cart import Cart
from .forms import CartAddProductForm


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=item,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        messages.success(request, 'Success')
    else:
        messages.info(request, 'NoSuccess')
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
