from django.urls import path, include
from . import views

urlpatterns = [
	path('Novo_grupo', views.Novo_grupo, name='Novo_grupo'),
	path('Entrar_grupo/<uuid:uuid>', views.Entrar_grupo, name='Entrar_grupo'),
	path('Sair_grupo/<uuid:uuid>', views.Sair_grupo, name='Sair_grupo'),
	path('Remover_grupo/<uuid:uuid>', views.Remover_grupo, name='Remover_grupo'),
	path('Abrir_chat_pub/<uuid:uuid>', views.Abrir_chat_pub, name='Abrir_chat_pub'),
	path('chat/excluir_mensagem_pub/<mensagem_id>/', views.excluir_mensagem_pub, name='excluir_mensagem_pub')
]