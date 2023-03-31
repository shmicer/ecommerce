from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import UserCreationForm, UserEditForm

from orders.models import Order

from .models import Address

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        cd = form.cleaned_data
        user = authenticate(email=cd['email'], password=cd['password1'])
        login(self.request, user)
        return redirect('home')
#
# class RegisterUser(View):
#     template_name = 'registration/register.html'
#
#     def get(self, request):
#         context = {
#             'form': UserCreationForm()
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             cd = form.cleaned_data
#             user = authenticate(email=cd['email'], password=cd['password1'])
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Not valid')
#             form = UserCreationForm()
#         return render(request, self.template_name, {'form': form})


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


