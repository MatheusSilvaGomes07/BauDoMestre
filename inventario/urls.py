from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="divisoes"),
    path("Mapas", views.mapas, name="mapas"),
    path("Criaturas", views.criaturas, name="criaturas"),
    path("Documentos", views.documentos, name="documentos"),
    path("Imagens", views.imagens, name="imagens"),
    path("Musicas", views.musicas, name="musicas"),
    path("<str:div>/<str:pasta>", views.visualizar_pasta, name="visualizar_pasta"),
    path("pasta/deletar/<int:id>", views.deletar_pasta, name="deletar_pasta"),
    path("arquivo/deletar/<int:id>/<str:div>/<int:id_pasta>", views.deletar_arquivo, name="deletar_arquivo"),
    path("editar/Pasta/<int:id_pasta>", views.edit_pasta, name="editar_pasta"),



]
