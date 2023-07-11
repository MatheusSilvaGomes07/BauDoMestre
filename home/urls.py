from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name = 'home'),
    path('mural', views.mural, name = 'mural'),
    path("CriarCampanhas/", views.criarCampanhas, name="criarCampanhas"),
    path('teste', views.teste, name='teste'),
    path('usuario', views.usuario, name = 'usuario'),
]
