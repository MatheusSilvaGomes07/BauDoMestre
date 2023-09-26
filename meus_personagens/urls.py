from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='meus_personagens'),
    path("criacao-char/", views.criacao_char, name="criacao_char"),
    path("personagem/dungeons&dragons/<int:id>", views.detail_charDnD, name='detail_char_dnd'),
    path("personagem/ordemparanormal/<int:id>", views.detail_charOrdemParanormal, name='detail_char_ordem'),
    path("personagem/tormenta20/<int:id>", views.detail_charTormenta, name='detail_char_tormenta'),
    path("personagem/callofcthulhu/<int:id>", views.detail_charCoC, name='detail_char_coc'),
    
] 
