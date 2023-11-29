from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from home.models import Perfil

class SolicitacaoAmizade(models.Model):
    de_usuario = models.ForeignKey(User, related_name='solicitacoes_enviadas', on_delete=models.CASCADE)
    para_usuario = models.ForeignKey(User, related_name='solicitacoes_recebidas', on_delete=models.CASCADE)
    aceita = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.de_usuario.username} -> {self.para_usuario.username}"

    
class Amigo(models.Model):
    usuario = models.ForeignKey(User, related_name='amigos', on_delete=models.CASCADE)
    amigo = models.ForeignKey(User, related_name='amigos_de', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, default=None)
    fotoConta = models.FileField(max_length=200, default="Indefinido")
    nomeAmigo = models.CharField(max_length=200, default='None')


    class Meta:
        unique_together = ('usuario', 'amigo')

    def save(self, *args, **kwargs):
        request = self.amigo.id
        perfil = Perfil.objects.get(id=request)
        nome = User.objects.get(id=request).username

        self.nomeAmigo = nome
        self.fotoConta = perfil.fotoConta
        self.slug = perfil.slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.username} -> {self.amigo.username}"
    
@receiver(post_save, sender=Perfil)
def atualizar_amigo(sender, instance, **kwargs):
    amigos = Amigo.objects.filter(amigo=instance.id)
    for amigo in amigos:
        amigo.fotoConta = instance.fotoConta
        amigo.save()
