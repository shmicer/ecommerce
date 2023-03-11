from django.db import models

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category': self.name})


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    category = models.ForeignKey('core.Category', on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey('core.Manufacturer', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'product_id': self.pk})

    def get_remove_from_cart_url(self):
        return reverse('remove_from_cart', kwargs={'product_id': self.pk})

    def get_increase_quantity(self):
        return reverse('increase_quantity', kwargs={'product_id': self.pk})

    def get_decrease_quantity(self):
        return reverse('decrease_quantity', kwargs={'product_id': self.pk})









