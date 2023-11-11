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

    def adicionar_usuario_ao_grupo(self, user):
        if user not in self.membros.all():
            self.membros.add(user)
            self.save()

class Mensagem(models.Model):
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	tempo = models.DateTimeField(auto_now_add=True)
	conteudo = models.TextField()
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class SolicitacaoEntrada(models.Model):
    de_usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='solicitacoes_enviadas_campanha')
    para_campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name='solicitacoes_entrada')
    status = models.CharField(max_length=20, default='Pendente')
    
    def aceitar_solicitacao(self):
        self.status = 'Aceita'
        self.save()

        # Obtém a campanha associada à solicitação
        campanha = self.para_campanha

        # Verifica se a campanha tem um grupo associado
        if hasattr(campanha, 'grupo'):
            grupo = campanha.grupo
            grupo.adicionar_usuario_ao_grupo(self.de_usuario.nomePerfil.nomePerfil)
            
            # Adicione uma declaração de impressão para verificar se o método está sendo chamado
            print(f"Usuário {self.de_usuario.nomePerfil.nomePerfil} adicionado ao grupo {grupo.uuid}")
