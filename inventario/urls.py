from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="divisoes"),
    path("mapas", views.mapas, name="mapas"),
    path("criaturas", views.criaturas, name="criaturas"),
    path("documentos", views.documentos, name="documentos"),
    path("imagens", views.imagens, name="imagens"),
    path("musicas", views.musicas, name="musicas"),
    path("mapas/<str:pasta>", views.visualizar_pasta, name="visualizar_pasta"),
    path("mapas/deletar/<int:id>", views.deletar, name="deletar"),

]
