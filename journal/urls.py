from django.urls import path

from . import views

app_name = 'journal'
urlpatterns = [
    path('', views.view_resources, name='view_resources'),
    path('new-resource/', views.create_new_resource, name='create_new_resource'),
]