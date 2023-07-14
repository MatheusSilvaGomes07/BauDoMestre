from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os


# Model do Usuário
class Perfil(models.Model):
    nomePerfil = models.ForeignKey(User, on_delete=models.CASCADE)
    SESSION_CHOICES = (
        ('online', 'Online'),
        ('presencial', 'Presencial'),
    )

    PLAYER_TYPE_CHOICES = (
        ('mestre', 'Mestre'),
        ('jogador', 'Jogador'),
        ('ambos', 'Ambos'),
    )

    RPG_SYSTEM_CHOICES = (
        ('dnd', 'Dungeons & Dragons'),
        ('tormenta20', 'Tormenta20'),
        ('ordem_par', 'Ordem Paranormal'),
        ('cthulhu', 'Call of Cthulhu'),
        ('outros', 'Outros'),
    )

    fotoConta = models.ImageField(upload_to='static/img/fotoUser')
    tipo_sessao = models.CharField(max_length=20, choices=SESSION_CHOICES, blank=True)
    tipo_player = models.CharField(max_length=20, choices=PLAYER_TYPE_CHOICES, blank=True)
    descricao = models.TextField(blank=True)
    sistema_rpg = models.CharField(max_length=20, choices=RPG_SYSTEM_CHOICES, blank=True)  


# Model do Mural
class Campanha(models.Model):
    nomeMestre = models.ForeignKey(User, on_delete=models.CASCADE)
    SISTEMAS_RPG_CHOICES = (
        ('Dungeons & Dragons', 'Dungeons & Dragons'),
        ('Ordem Paranormal', 'Ordem Paranormal'),
        ('Tormenta20', 'Tormenta20'),
        ('Call of Cthulu', 'Call of Cthulu'),
        ('Outro', 'Outro')
    )
    AMBIENTES_RPG_CHOICES = (
        ('Online', 'Online'),
        ('Presencial', 'Presencial')
    )
    GENERO_RPG_CHOICES = (
        ('Aventura', 'Aventura'),
        ('Comédia', 'Comédia'),
        ('Drama', 'Drama'),
        ('Fantasia', 'Fantasia'),
        ('Histórico', 'Histórico'),
        ('Mistério', 'Mistério'),
        ('Suspense', 'Suspense'),
        ('Terror', 'Terror'),
    )
    nomeCampanha = models.CharField(max_length=52)
    sistemaCampanha = models.CharField(max_length=100, choices=SISTEMAS_RPG_CHOICES)
    descricaoCampanha = models.TextField(max_length=256)
    fotoCampanha = models.ImageField(upload_to='static/img/FotoCampanha/')
    ambienteCampanha = models.CharField(max_length=100, choices=AMBIENTES_RPG_CHOICES)
    numeroJogadores = models.IntegerField()
    diasSessao = models.CharField(max_length=52)
    generoRPG = models.CharField(max_length=100, choices=GENERO_RPG_CHOICES)

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(nomePerfil=instance, descricao='Indefinido', tipo_sessao='Indefinido', tipo_player='Indefinido', sistema_rpg='Indefinido', fotoConta ='static/img/fotoUser/Ain.png')
