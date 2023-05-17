from django.urls import path

from . import views
from orders.api import views as api_views


urlpatterns = [
    path('checkout', views.OrderCheckoutView.as_view(), name='checkout'),
    path('create/', views.OrderView.as_view(), name='order_create'),
    path('api/v1/orderlist/', api_views.OrderListAPIView.as_view()),

]