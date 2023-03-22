from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Address(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    is_current = models.BooleanField(default=False)
    is_pickpoint = models.BooleanField(default=False)
    owner = models.ManyToManyField('account.User', blank=True)

    def __str__(self):
        return '{}'.format(self.id)
