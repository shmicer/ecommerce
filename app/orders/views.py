from django.contrib import messages
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm

from cart.cart import Cart


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.instance.customer = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(product=item['product'],
                                         price=item['price'],
                                         order_id=order.id,
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'create.html', {'cart': cart, 'form': form})


def order_detail(request):
    return render(request, 'order_info.html')
