from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('mural', views.mural, name = 'mural'),
    path('criarCampanhas/', views.criarCampanhas, name="criarCampanhas"),
    path('teste', views.teste, name='teste'),
    path('usuario', views.usuario, name = 'usuario'),
    path('editarConta', views.editarconta, name='editarconta'),
    path('buscarMesa/', views.buscarmesa, name='buscarmesa'),
    path('buscarMesa/detalhes_campanha/<int:pk>/', views.buscarmesa, name='detalhes_campanha'),
]
