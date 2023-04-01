from django.urls import path

from . import views


urlpatterns = [

    path('register', views.RegisterUser.as_view(), name="register"),
    path('edit/', views.edit_user, name='edit-profile'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderView.as_view(), name='order-info'),
    path('my-addressbook/', views.AddressView.as_view(), name='addresses'),
    path('add-address/', views.AddAddressView.as_view(), name='add-address'),
    path('edit-address/<int:pk>', views.UpdateAddressView.as_view(), name='edit-address'),

    ]