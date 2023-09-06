from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='meus_personagens'),
    path("criacao-char/", views.criacao_char, name="criacao_char"),
    path("personagem/dnd/<int:id>", views.detail_charDnD, name='detail_char_dnd'),
    path("personagem/ordem/<int:id>", views.detail_charOrdemParanormal, name='detail_char_ordem'),
]
