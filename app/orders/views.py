from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from django.core.mail import send_mail

from cart.cart import Cart

from account.models import Address



def checkout(request):
    return render(request, 'create.html')


def create_order(request):
    cart = Cart(request)
    addresses = Address.objects.filter(owner=request.user, is_pickpoint=False)
    pickpoints = Address.objects.filter(is_pickpoint=True)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.instance.customer = request.user
            order = form.save()
            send_mail(
                f'Order {order.id}',
                'Here is the message.',
                'from@example.com',
                [order.email],
                fail_silently=False,
            )
            for item in cart:
                OrderItem.objects.create(product=item['product'],
                                         price=item['price'],
                                         order_id=order.id,
                                         quantity=item['quantity'],
                                         total=item['price'] * item['quantity'])
            cart.clear()
            return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm
    context = {'cart': cart,'form': form, 'pickpoints': pickpoints, 'addresses': addresses}
    return render(request, 'create.html', context=context)

