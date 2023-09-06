from django.contrib import admin
from .models import DnD, OrdemParanormal

@admin.register(DnD)
class DnDAdmin(admin.ModelAdmin):
    list_display = ('nomePerfil', 'nome')
    #list_filter = ('sistemaCampanha', 'generoRPG', 'ambienteCampanha')
    #search_fields = ('nomeCampanha',)

@admin.register(OrdemParanormal)
class OrdemAdmin(admin.ModelAdmin):
    list_display = ('nomePerfil', 'nome')