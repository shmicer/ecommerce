import uuid

from django.conf import settings
from django.core.cache import cache
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import UserCreationForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from orders.models import Order

from .models import Address

User = get_user_model()


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if not user.is_active:
            token = uuid.uuid4().hex
            redis_key = settings.ECOMMERCE_USER_CONFIRMATION_KEY.format(token=token)
            cache.set(redis_key, {'user_id': user.id}, timeout=settings.ECOMMERCE_USER_CONFIRMATION_TIMEOUT)

            confirm_link = self.request.build_absolute_uri(
                reverse_lazy(
                    'register_confirm', kwargs={'token': token}
                )
            )
            user.send_confirmation_email(confirm_link)
        return super().form_valid(form)

def register_confirm(request, token):
    redis_key = settings.ECOMMERCE_USER_CONFIRMATION_KEY.format(token=token)
    user_info = cache.get(redis_key) or {}

    if user_id := user_info.get("user_id"):
        user = get_object_or_404(User, id=user_id)
        user.is_active = True
        user.save(update_fields=["is_active"])
        return redirect(to=reverse_lazy("login"))
    else:
        return redirect(to=reverse_lazy("register"))

class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user).select_related('customer')
        return context


class OrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'account/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user).select_related('customer')
        return context


class OrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'account/order-items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = context['order'].items.select_related('product')
        context['delivery_type'] = 'Address Delivery' if not context['order'].address.is_pickpoint else 'Pickpoint Delivery'
        context['address'] = context['order'].address.address
        context['items_count'] = sum([item.quantity for item in context['order_items']])
        return context


class AddressView(LoginRequiredMixin, ListView):
    model = Address
    context_object_name = 'addresses'
    template_name = 'account/addressbook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = context['addresses'].filter(is_pickpoint=False, owner=self.request.user)
        return context


class AddAddressView(LoginRequiredMixin, CreateView):
    model = Address
    template_name = 'account/address-form.html'
    fields = ['address', 'city', 'postcode']
    success_url = reverse_lazy('addresses')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner.add(self.request.user)
        return super().form_valid(form)


class UpdateAddressView(LoginRequiredMixin, UpdateView):
    model = Address
    template_name = 'account/address-form.html'
    fields = ['address', 'city', 'postcode']
    success_url = reverse_lazy('addresses')

    def form_valid(self, form):
        return super().form_valid(form)


def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        return render(request,
                      'account/edit-profile.html',
                      {'user_form': user_form})


