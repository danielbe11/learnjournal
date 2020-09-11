from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'journal'
urlpatterns = [
    path('', views.view_resources, name='view_resources'),
    path('resource-<int:resource_id>/', views.detail_resources, name='detail_resources'),
    path('new-resource/', views.create_new_resource, name='create_new_resource'),
    path('resource-<int:resource_id>/edit-resource/', views.edit_resource, name='edit_resource'),
    path('resource-<int:resource_id>/delete-resource/', views.delete_resource, name='delete_resource'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)