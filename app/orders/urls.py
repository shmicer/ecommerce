from django.urls import path

from . import views


urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('create/', views.create_order, name='order_create'),
]