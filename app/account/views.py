from decimal import Decimal

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .forms import RegisterUserForm, LoginUserForm, UserEditForm
from django.contrib.auth.views import LoginView

from orders.models import Order


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'


def logout_user(request):
    logout(request)
    return redirect('home')


class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user).select_related('customer')
        return context


class OrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = context['order'].items.all().select_related('product')
        context['total_items'] = sum([item.quantity for item in context['order_items']])
        return context


def order_view(request, pk):
    order = Order.objects.get(customer=request.user, pk=pk)
    order_items = order.items.all().select_related('product')
    total_items = sum([item.quantity for item in order_items])
    context = {'order': order, 'order_items': order_items, 'total_items': total_items}
    return render(request, 'order_info.html', context)


def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        return render(request,
                      'edit_profile.html',
                      {'user_form': user_form})


