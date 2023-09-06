from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    nomePerfil = models.ForeignKey(User, on_delete=models.CASCADE)
    

    class Meta:
        abstract = True
        unique_together = ('nome',)

class DnD(Personagem):
    #Dados Iniciais
    vida = models.IntegerField(null=True)
    classe = models.CharField(max_length=100)
    sub_classe = models.CharField(max_length=100, blank=True, null=True)
    nivel = models.IntegerField(validators=[MinValueValidator(1)])
    raca = models.CharField(max_length=100, null=True)
    sub_raca = models.CharField(max_length=100, blank=True, null=True)
    xp = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)

    #Atributos
    forca = models.IntegerField(default=0)
    dex = models.IntegerField(default=0)
    const = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    sab = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)

    inspiracao = models.BooleanField(default=False)

    #Saving Throws
    forcaSalvaguarda = models.BooleanField(default=False)
    dexSalvaguarda = models.BooleanField(default=False)
    constSalvaguarda = models.BooleanField(default=False)
    intSalvaguarda = models.BooleanField(default=False)
    sabSalvaguarda = models.BooleanField(default=False)
    carismaSalvaguarda = models.BooleanField(default=False)

    #Pericias
    acrobacia = models.BooleanField(default=False)
    adestrarAnimais = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    atletismo = models.BooleanField(default=False)
    enganacao = models.BooleanField(default=False)
    historia = models.BooleanField(default=False)
    intuicao = models.BooleanField(default=False)
    intimidacao = models.BooleanField(default=False)
    investigacao = models.BooleanField(default=False)
    medicina = models.BooleanField(default=False)
    natureza = models.BooleanField(default=False)
    percepcao = models.BooleanField(default=False)
    atuacao = models.BooleanField(default=False)
    persuasao = models.BooleanField(default=False)
    religiao = models.BooleanField(default=False)
    prestigitacao = models.BooleanField(default=False)
    furtividade = models.BooleanField(default=False)
    sobrevivencia = models.BooleanField(default=False)


    proficienciasFerramentas = models.TextField(null=True, blank=True)
    outrasProf_Linguagens = models.TextField(null=True, blank=True)

    #Coluna do meio
    ca = models.IntegerField(default=0)
    movi = models.FloatField(blank=True, null=True)
    vidaTemp = models.IntegerField(null=True, blank=True)
    hitDice = models.IntegerField(null=True, blank=True)
    hitDiceType_Options = [
        ('d4', 'd4'),
        ('d6', 'd6'),
        ('d8', 'd8'),
        ('d10', 'd10'),
        ('d12', 'd12'),
    ]
    hitDiceType = models.CharField(max_length=4, choices=hitDiceType_Options, default='d4')

    deathSucess1 = models.BooleanField(default=False)
    deathSucess2 = models.BooleanField(default=False)
    deathSucess3 = models.BooleanField(default=False)

    deathFailure1 = models.BooleanField(default=False)
    deathFailure2 = models.BooleanField(default=False)
    deathFailure3 = models.BooleanField(default=False)


    #Ataques
    nomeAtk1 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk1 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk1 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk2 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk2 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk2 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk3 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk3 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk3 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk4 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk4 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk4 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk5 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk5 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk5 = models.CharField(max_length=100, blank=True, null=True)


    #Dinheiro
    pc = models.IntegerField(default=0)
    pp = models.IntegerField(default=0)
    pe = models.IntegerField(default=0)
    po = models.IntegerField(default=0)
    pl = models.IntegerField(default=0)


    #inventario
    inventario = models.TextField(null=True, blank=True)

    



    #Caracteristicas
    personalidade = models.CharField(null=True, blank=True, max_length=350)
    ideias = models.CharField(null=True, blank=True, max_length=350)
    vinculos = models.CharField(null=True, blank=True, max_length=350)
    fraquezas = models.CharField(null=True, blank=True, max_length=350)

    #Características e Talentos
    caracteristicas = models.TextField(null=True, blank=True)


class OrdemParanormal(Personagem):
    nex = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(0)])