from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='meus_personagens'),
    path("criacao-char/", views.criacao_char, name="criacao_char"),
    path("personagem/dungeons&dragons/<int:id>", views.detail_charDnD, name='detail_char_dnd'),
    path("personagem/ordemparanormal/<int:id>", views.detail_charOrdemParanormal, name='detail_char_ordem'),
    path("personagem/tormenta20/<int:id>", views.detail_charTormenta, name='detail_char_tormenta'),
    path("personagem/callofcthulhu/<int:id>", views.detail_charCoC, name='detail_char_coc'),
    path("editarPersonagem/dungeons&dragons/<int:id>", views.edit_dnd, name="edit_dnd"),
    path("editarPersonagem/ordemparanormal/<int:id>", views.edit_ordem, name="edit_ordem"),
    path("editarPersonagem/tormenta20/<int:id>", views.edit_tormenta20, name="edit_tormenta20"),
    path("editarPersonagem/callofcthulhu/<int:id>", views.edit_coc1920, name="edit_coc1920"),
    path("deletarPersonagem/<str:rpg>/<int:id>", views.deletarChar, name="deletar_char"),



    
] 
