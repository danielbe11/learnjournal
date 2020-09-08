from django.urls import path

from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.view_resources, name='view_resources'),
    path('<int:resource_id>/', views.detail_resources, name='detail_resources'),
    path('new-resource/', views.create_new_resource, name='create_new_resource'),
    path('<int:resource_id>/edit-resource/', views.edit_resource, name='edit_resource'),
    path('<int:resource_id>/delete-resource/', views.delete_resource, name='delete_resource'),
    ]