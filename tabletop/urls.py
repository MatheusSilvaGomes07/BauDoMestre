from django.urls import path
from . import views

urlpatterns = [
    path('<int:campaign_id>/', views.enter_campaign, name='enter_campaign'),
    path('map/<int:map_id>/', views.load_map, name='load_map'),
    path('token/<int:token_id>/move/', views.move_token, name='move_token'),
    path('deletar/<int:campaign_id>/<int:map_id>/', views.deletar_mapa, name='deletar_mapa'),
    path('criar_pasta_criaturas/<int:campaign_id>/', views.criarPastaCriaturas, name='criar_pasta_criaturas'),
    path('criar_ficha/<int:campaign_id>/<int:pasta_id>/', views.criar_personagem, name='criar_personagem'),
    path('map/place_token/<int:map_id>/<int:personagem_id>/', views.place_token, name='place_token'), 
    path('deletar_personagem/<int:campaign_id>/<int:personagem_id>/', views.deletar_personagem_campanha, name="deletar_personagem_campanha"),
]
