from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_forms.html'),
         name="password_reset"
         ),
    # path('login', views.user_login, name='login'),
    # path('logout', views.logout_user, name='logout'),
    path('register', views.RegisterUser.as_view(), name="register"),
    path('edit/', views.edit_user, name='edit_profile'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderView.as_view(), name='order_info')




    ]