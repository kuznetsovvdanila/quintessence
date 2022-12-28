import django.conf.urls.static
from django.urls import path
from . import views
from quintessence import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('project_manager/', views.project_manager, name='project_manager'),
    path('request_handler/', views.request_handler, name='request_handler'),
] + django.conf.urls.static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)