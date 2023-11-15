from django.urls import path, include
from . import views

urlpatterns = [
	path('Novo_grupo', views.Novo_grupo, name='Novo_grupo'),
	path('Sair_grupo/<uuid:uuid>', views.Sair_grupo, name='Sair_grupo'),
	path('Remover_grupo/<uuid:uuid>', views.Remover_grupo, name='Remover_grupo'),
	path('Abrir_chat_pub/<uuid:uuid>', views.Abrir_chat_pub, name='Abrir_chat_pub'),
	path('chat/excluir_mensagem_pub/<mensagem_id>/', views.excluir_mensagem_pub, name='excluir_mensagem_pub'),
    path('chat/gerenciar_solicitacoes/', views.gerenciar_solicitacoes, name='gerenciar_solicitacoes'),
    path('chat/gerenciar_solicitacoes/<int:campanha_id>/', views.gerenciar_solicitacoes, name='gerenciar_solicitacoes_campanha'),
    path('enviar_solicitacao/<int:campanha_id>/', views.enviar_solicitacao, name='enviar_solicitacao'),
    path('aceitar_solicitacao_camp/<int:solicitacao_id>/', views.aceitar_solicitacao_camp, name='aceitar_solicitacao_camp'),
    path('recusar_solicitacao_camp/<int:solicitacao_id>/', views.recusar_solicitacao_camp, name='recusar_solicitacao_camp'),
]