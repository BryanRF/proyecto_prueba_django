from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import pagina_base

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', pagina_base, name='pagina_base'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)