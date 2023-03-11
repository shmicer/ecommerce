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

#
# def decrease_quantity(request, pk):
#     item = get_object_or_404(Product, pk=pk)
#     order = Order.objects.get_or_create(customer=request.user, ordered=False)[0]
#     order_item = OrderItem.objects.filter(
#         product=item,
#         customer=request.user,
#         ordered=False
#     )[0]
#     if order:
#         if order_item.quantity > 1:
#             order_item.quantity -= 1
#             order_item.save()
#             messages.success(request, 'Item quantity is updated')
#         else:
#             order_item.delete()
#             messages.success(request, 'This item was removed from your cart.')
#         return redirect('cart')
#     else:
#         messages.info(request, 'You do not have an Order')
#         return redirect('cart')
#
#
# def increase_quantity(request, pk):
#     item = get_object_or_404(Product, pk=pk)
#     order = Order.objects.get_or_create(customer=request.user, ordered=False)[0]
#     order_item = OrderItem.objects.filter(
#         product=item,
#         customer=request.user,
#         ordered=False
#     )[0]
#     if order:
#         order_item.quantity += 1
#         order_item.save()
#         messages.success(request, 'Item quantity is updated')
#         return redirect('cart')
#     else:
#         messages.info(request, 'You do not have an Order')
#         return redirect('cart')