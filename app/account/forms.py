

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.utils.translation import gettext_lazy as _

from .models import Address, PickPoint

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email']

# class LoginUserForm(forms.Form):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(label='Password')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['address', 'city', 'postcode']