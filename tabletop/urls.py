from django.urls import path
from . import views

urlpatterns = [
    path('<int:campaign_id>/', views.enter_campaign, name='enter_campaign'),
    path('map/<int:map_id>/', views.load_map, name='load_map'),
    path('token/<int:token_id>/move/', views.move_token, name='move_token'),
]
