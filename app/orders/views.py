from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView

from .models import OrderItem, Order
from .forms import OrderCreateForm

from cart.cart import Cart

from account.models import Address
from django.views.generic.edit import FormView


class OrderCreateView(FormView):
    model = Order
    template_name = 'create.html'
    form_class = OrderCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.filter(owner=self.request.user.id, is_pickpoint=False)
        context['pickpoints'] = Address.objects.filter(is_pickpoint=True)
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        order.customer = self.request.user if self.request.user.is_authenticated else None
        order.save()
        for item in cart:
            OrderItem.objects.create(product=item['product'],
                                     price=item['price'],
                                     order_id=order.id,
                                     quantity=item['quantity'],
                                     total=item['price'] * item['quantity'])
        cart.clear()
        order.send_email()
        return super().form_valid(form)
