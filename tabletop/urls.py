# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tabletop_view, name='tabletop_view'),
    path('update_object_position/', views.update_object_position, name='update_object_position'),
    path('delete_all_images/', views.delete_all_images, name='delete_all_images'),
]