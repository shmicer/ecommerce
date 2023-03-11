from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.create_order, name='order_create'),
    path('order_info', views.order_detail, name='order_info')
]