from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm

from cart.cart import Cart

from account.models import Address


def checkout(request):
    return render(request, 'create.html')


def create_order(request):
    cart = Cart(request)
    owner = request.user if request.user.is_authenticated else None
    addresses = Address.objects.filter(owner=owner, is_pickpoint=False)
    pickpoints = Address.objects.filter(is_pickpoint=True)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.customer = owner
            order.save()
            for item in cart:
                OrderItem.objects.create(product=item['product'],
                                         price=item['price'],
                                         order_id=order.id,
                                         quantity=item['quantity'],
                                         total=item['price'] * item['quantity'])
            cart.clear()
            order.send_email()
            return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm
    context = {'cart': cart,'form': form, 'pickpoints': pickpoints, 'addresses': addresses}
    return render(request, 'create.html', context=context)


