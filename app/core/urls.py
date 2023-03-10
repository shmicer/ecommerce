from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('checkout', views.checkout, name='checkout'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name='product'),
    path('<str:category>/', views.HomeView.as_view(), name='category'),

    ]