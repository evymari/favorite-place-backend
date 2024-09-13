from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls')),  # Incluye las URLs de la app 'users'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
