from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView

from .forms import RegisterUserForm, LoginUserForm, UserEditForm

from orders.models import Order


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})


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
    order = get_object_or_404(Order, customer=request.user, pk=pk)
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


