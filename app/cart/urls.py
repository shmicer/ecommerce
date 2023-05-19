from django.urls import path

from . import views


urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/<product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('decrease_quantity/<product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<product_id>/', views.increase_quantity, name='increase_quantity'),
]