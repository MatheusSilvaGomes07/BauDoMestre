from django.contrib import admin
from .models import Campanha, Perfil

@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    list_display = ('nomeMestre', 'nomeCampanha', 'sistemaCampanha', 'ambienteCampanha', 'fotoCampanha')
    list_filter = ('sistemaCampanha', 'generoRPG', 'ambienteCampanha')
    search_fields = ('nomeCampanha',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nomePerfil', 'tipo_player', 'tipo_sessao', 'sistema_rpg')
    list_filter = ('tipo_sessao', 'tipo_player', 'sistema_rpg')
