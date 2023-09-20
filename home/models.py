import os
import shutil
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


# Model do Perfil do usuário
class Perfil(models.Model):
    nomePerfil = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(User, unique=True)
    SESSION_CHOICES = (
        ('Online', 'Online'),
        ('Presencial', 'Presencial'),
    )

    PLAYER_TYPE_CHOICES = (
        ('Mestre', 'Mestre'),
        ('Jogador', 'Jogador'),
        ('Ambos', 'Ambos'),
    )

    RPG_SYSTEM_CHOICES = (
        ('Dungeons & Dragons', 'Dungeons & Dragons'),
        ('Tormenta20', 'Tormenta20'),
        ('Ordem Paranormal', 'Ordem Paranormal'),
        ('Call of Cthulhu', 'Call of Cthulhu'),
        ('Outros', 'Outros'),
    )

    fotoConta = models.ImageField(upload_to='static/img/fotoUser')
    tipo_sessao = models.CharField(max_length=20, choices=SESSION_CHOICES, null=True)
    tipo_player = models.CharField(max_length=20, choices=PLAYER_TYPE_CHOICES, null=True)
    descricao = models.TextField(max_length=256, null=True)
    sistema_rpg = models.CharField(max_length=20, choices=RPG_SYSTEM_CHOICES, null=True)
    idade = models.IntegerField(null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nomePerfil.username)
        super(Perfil, self).save(*args, **kwargs)


# Model das Campanhas
class Campanha(models.Model):
    nomeMestre = models.ForeignKey(Perfil, on_delete=models.CASCADE)
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
        ('Fantasia', 'Fantasia'),
        ('Histórico', 'Histórico'),
        ('Mistério', 'Mistério'),
        ('Suspense', 'Suspense'),
        ('Terror', 'Terror'),
    )
    nomeCampanha = models.CharField(max_length=52, null=True)
    sistemaCampanha = models.CharField(max_length=100, choices=SISTEMAS_RPG_CHOICES, null=True)
    descricaoCampanha = models.TextField(max_length=256, null=True)
    fotoCampanha = models.ImageField(upload_to='static/img/FotoCampanha/', null=True)
    ambienteCampanha = models.CharField(max_length=100, choices=AMBIENTES_RPG_CHOICES, null=True)
    numeroJogadores = models.IntegerField(null=True)
    diasSessao = models.CharField(max_length=52, null=True)
    generoRPG = models.CharField(max_length=100, choices=GENERO_RPG_CHOICES, null=True)

# Atualiza o perfil do usuário assim que a conta é criada
@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created and not Perfil.objects.filter(nomePerfil=instance).exists():
        perfil = Perfil.objects.create(nomePerfil=instance, descricao='Indefinido', tipo_sessao='Indefinido', tipo_player='Indefinido', sistema_rpg='Indefinido', idade='0')
        
        # Cria a foto única para cada usuário
        nome_usuario = instance.username
        caminho_origem = 'static/img/Ain.png'
        caminho_destino = f'static/img/fotoUser/{nome_usuario}.png'
        
        try:
            shutil.copyfile(caminho_origem, caminho_destino)
        except FileNotFoundError:
            print("Arquivo 'Ain.png' não encontrado.")

        perfil.fotoConta = caminho_destino
        perfil.save()
