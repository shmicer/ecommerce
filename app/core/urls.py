from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('checkout', views.checkout, name='checkout'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name='product'),
    path('category-list',views.CategoryView.as_view(), name='category-list'),
    path('brand-list',views.BrandView.as_view(), name='brand-list'),
    path('product-list',views.ProductView.as_view(), name='product-list'),
    path('<str:category>/', views.HomeView.as_view(), name='category'),

    ]