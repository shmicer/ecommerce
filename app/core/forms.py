from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(label='Email')
    username = forms.CharField(label='Username')
    # first_name = forms.CharField(label='First name')
    # last_name = forms.CharField(label='Last name')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Repeat password')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
