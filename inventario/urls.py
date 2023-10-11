from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="divisoes"),
    path("mapas", views.mapas, name="mapas"),
    path("criaturas", views.criaturas, name="criaturas"),
    path("documentos", views.documentos, name="documentos"),
    path("imagens", views.imagens, name="imagens"),
    path("musicas", views.musicas, name="musicas"),
    path("<str:div>/<str:pasta>", views.visualizar_pasta, name="visualizar_pasta"),
    path("pasta/deletar/<int:id>", views.deletar_pasta, name="deletar_pasta"),

]
