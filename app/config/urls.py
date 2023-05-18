from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change_forms.html'),
        name='change-password'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_changed.html'),
        name='password_change_done'
    ),
    path('', include('core.urls')),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('account/', include('account.urls')),
    path('', include('social_django.urls', namespace="social")),
    path('__debug__/', include('debug_toolbar.urls')),
    path('search', include('search.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
