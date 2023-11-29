from django.contrib import admin
from django.urls import path, include , re_path
from geral import views
from geral.api import viewsets 

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api', include('geral.api.urls')),
    path('admin/', admin.site.urls),
    path('view_test/',views.view_test, name = "test_view"),
    path('cadastrar/', viewsets.query),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

