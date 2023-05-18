from django.urls import path

from . import views
from core.api import views as api_views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name='product'),
    path('category-list', views.CategoryView.as_view(), name='category-list'),
    path('brand-list', views.ManufacturerView.as_view(), name='brand-list'),
    path('product-list', views.ProductView.as_view(), name='product-list'),
    path('filter-data', views.filter_data, name='filter-data'),
    path('<str:category>/', views.HomeView.as_view(), name='category'),
    # path('search', views.search, name='search'),
    path('api/v1/productlist/', api_views.ProductListAPIView.as_view()),
    path('api/v1/categorylist/', api_views.CategoryListAPIView.as_view()),
    path('api/v1/manufacturerlist/', api_views.ManufacturerListAPIView.as_view()),
    ]