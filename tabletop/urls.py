from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_map, name='create_map'),
    path('<int:map_id>/', views.enter_map, name='enter_map'),
    path('upload_token/', views.upload_token, name='upload_token'),
    path('<int:map_id>/update_token_position/', views.update_token_position, name='update_token_position'),
    path('delete_all_tokens/', views.delete_all_images, name='delete_all_tokens'),
]
