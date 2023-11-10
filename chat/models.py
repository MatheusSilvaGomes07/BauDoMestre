from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from home.models import Campanha, Perfil


User = get_user_model()

class Grupo(models.Model):
	uuid = models.UUIDField(default=uuid4, editable=False)
	membros = models.ManyToManyField(User)
	criador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='grupos_criados')
	publico = models.BooleanField(default=False)
	campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name='chats', null=True)

	def adicionar_user(request, user):
		self.membros.add(user)
		self.save()
		return

	def remover_user(request, user):
		self.membros.remove(user)
		self.save()
		return


class Mensagem(models.Model):
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	tempo = models.DateTimeField(auto_now_add=True)
	conteudo = models.TextField()
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)



class SolicitacaoEntrada(models.Model):
    de_usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='solicitacoes_enviadas_campanha')
    para_campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name='solicitacoes_entrada')
    status = models.CharField(max_length=20, default='Pendente')