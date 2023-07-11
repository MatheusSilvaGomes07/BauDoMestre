from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    sistemaCampanha = models.CharField(max_length=100, choices= SISTEMAS_RPG_CHOICES)
    descricaoCampanha = models.CharField(max_length=256)
    fotoCampanha = models.ImageField(upload_to='static/img/FotoCampanha/')
    ambienteCampanha = models.CharField(max_length=100, choices= AMBIENTES_RPG_CHOICES)
    numeroJogadores = models.IntegerField()
    diasSessao = models.CharField(max_length=52)
    generoRPG = models.CharField(max_length=100, choices=GENERO_RPG_CHOICES)
    
    def __str__(self):
        return f"Nome da Campanha: {self.nomeCampanha}, Mestre: {self.nomeMestre.username}, Email do Mestre: {self.nomeMestre.email}"

