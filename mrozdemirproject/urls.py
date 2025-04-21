from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # portfolio app'ine yönlendirme
]

# Geliştirme ortamında media ve static dosyalarını göstermek için
if settings.DEBUG:
    # Media dosyaları
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Static dosyalar
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])