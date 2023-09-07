from django.contrib import admin
from .models import Grupo


@admin.register(Grupo)
class GrupoADM(admin.ModelAdmin):
    ('uuid')
    ('membros')
   

