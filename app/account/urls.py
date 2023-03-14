from django.urls import path

from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterUser.as_view(), name="register"),
    path('edit/', views.edit_user, name='edit_profile'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('order/<int:pk>', views.order_view, name='order_info')




    ]