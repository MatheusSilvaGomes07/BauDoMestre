# urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('enviar_solicitacao/<int:user_id>/', views.enviar_solicitacao, name='enviar_solicitacao'),
    path('listar_solicitacoes/', views.listar_solicitacoes, name='listar_solicitacoes'),
    path('aceitar_solicitacao/<int:solicitacao_id>/', views.aceitar_solicitacao, name='aceitar_solicitacao'),
    path('recusar_solicitacao/<int:solicitacao_id>/', views.recusar_solicitacao, name='recusar_solicitacao'),
    path('adicionar_amigo/<int:user_id>/', views.adicionar_amigo, name='adicionar_amigo'),
    path('remover_amigo/<int:user_id>/', views.remover_amigo, name='remover_amigo'),
    path('listar_amigos/', views.listar_amigos, name='listar_amigos'),
    path('Abrir_chat_privado/<int:user_id>/', views.Abrir_chat_Amigo, name='Abrir_chat_privado'),
    path('excluir_mensagem/<int:mensagem_id>/', views.excluir_mensagem_priv, name='excluir_mensagem'),
]
