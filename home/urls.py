from . import views
from django.urls import path
from inventario.views import index
from .views import excluir_jogador

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search', views.search_user, name='search_user'),
    path('search/usuario_busca/<int:pk>/', views.search_user, name='usuario_busca'),
    path('criarCampanhas/', views.criarCampanhas, name="criarCampanhas"),
    path('usuario', views.usuario, name = 'usuario'),
    path('editarConta', views.editarconta, name='editarconta'),
    path('buscarMesa/', views.buscarmesa, name='buscarmesa'),
    path('buscarMesa/detalhes_campanha/<int:id>/', views.detalhes_campanha, name='detalhes_campanha'),
    path('usuario/<slug:perfil_slug>/', views.exibir_perfil, name='exibir_perfil'),
    path('sobre-nos/', views.aboutus, name='sobre-nos' ),
    path('home/', views.home, name='home' ),
    path('inventario/', index, name='inventarioRedirect'),
    path('campanha/<int:campanha_id>/excluir-jogador/<int:jogador_id>/', excluir_jogador, name='excluir_jogador'),
    path('campanha/excluir/<int:campanha_id>/', views.excluir_campanha, name='excluir_campanha'),
]
