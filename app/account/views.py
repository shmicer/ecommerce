from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView


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