
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from .forms import UserCreationForm, UserEditForm

from orders.models import Order


class RegisterUser(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password1'])
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user).select_related('customer')
        return context

class OrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'profile/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.request.user).select_related('customer')
        return context


def order_view(request, pk):
    order = get_object_or_404(Order, customer=request.user, pk=pk)
    order_items = order.items.all().select_related('product')
    context = {'order': order, 'order_items': order_items}
    return render(request, 'profile/order-items.html', context)


def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        return render(request,
                      'profile/edit_profile.html',
                      {'user_form': user_form})


