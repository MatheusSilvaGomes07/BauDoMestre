from django.contrib import admin
from .models import Campanha
# Register your models here.
@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    list_display = ('nomeMestre', 'nomeCampanha', 'ambienteCampanha', 'fotoCampanha')
    list_filter = ('sistemaCampanha', 'generoRPG', 'ambienteCampanha')
    search_fields = ('nomeCampanha',)