from django.urls import path

from . import views
from orders.api import views as api_views


urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    # path('created/', views.OrderCreatedView.as_view(), name='created'),
    path('api/v1/orderlist/', api_views.OrderListAPIView.as_view()),

]