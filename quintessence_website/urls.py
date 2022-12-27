import django.conf.urls.static
from django.urls import path
from . import views
from quintessence import settings

urlpatterns = [
    path('', views.index, name='index')
] + django.conf.urls.static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)