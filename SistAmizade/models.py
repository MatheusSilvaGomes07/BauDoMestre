from django.db import models
from django.contrib.auth.models import User

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

    class Meta:
        unique_together = ('usuario', 'amigo')

    def __str__(self):
        return f"{self.usuario.username} -> {self.amigo.username}"