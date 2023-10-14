from django.db import models
from django.contrib.auth.models import User

class SolicitacaoAmizade(models.Model):
    de_usuario = models.ForeignKey(User, related_name='solicitacoes_enviadas', on_delete=models.CASCADE)
    para_usuario = models.ForeignKey(User, related_name='solicitacoes_recebidas', on_delete=models.CASCADE)
    aceita = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('de_usuario', 'para_usuario')

    def __str__(self):
        return f"{self.de_usuario.username} -> {self.para_usuario.username}"