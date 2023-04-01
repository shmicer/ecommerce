from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from .tasks import send_order_email_task


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.ForeignKey('account.Address', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def send_email(self):
        send_order_email_task.delay(
            self.email, self.id
        )



class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order', related_name='items', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('core.Product', related_name='order_items', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        total = self.price * self.quantity



