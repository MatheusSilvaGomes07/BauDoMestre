from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login, name= 'login'),
    path('cadastro', views.cadastro, name = 'cadastro'),
    path('mural', views.mural, name = 'mural'),
    path('teste', views.teste, name='teste'),
]
