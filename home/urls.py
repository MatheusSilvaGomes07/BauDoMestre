from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('search', views.search_user, name='search_user'),
    path('search/usuario_busca/<int:pk>/', views.search_user, name='usuario_busca'),
    path('mural', views.mural, name = 'mural'),
    path('criarCampanhas/', views.criarCampanhas, name="criarCampanhas"),
    path('usuario', views.usuario, name = 'usuario'),
    path('editarConta', views.editarconta, name='editarconta'),
    path('buscarMesa/', views.buscarmesa, name='buscarmesa'),
    path('buscarMesa/detalhes_campanha/<int:pk>/', views.buscarmesa, name='detalhes_campanha'),
    path('usuario/<slug:perfil_slug>/', views.exibir_perfil, name='exibir_perfil'),
]
