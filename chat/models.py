from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from home.models import Campanha



User = get_user_model()

class Grupo(models.Model):
    from home.models import Campanha
    uuid = models.UUIDField(default=uuid4, editable=False)
    membros = models.ManyToManyField(User)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='grupos_criados')
    publico = models.BooleanField(default=False)
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name='chats', null=True)

    def adicionar_usuario_ao_grupo(self, user):
        if user not in self.membros.all():
            self.membros.add(user)
            self.save()

             # Adicione um print para verificar se o usuário foi adicionado ao grupo
            print(f"Usuário {user} adicionado ao grupo {self.uuid}")
        else:
            # Adicione um print para indicar que o usuário já está no grupo
            print(f"Usuário {user} já está no grupo {self.uuid}")

class Mensagem(models.Model):
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	tempo = models.DateTimeField(auto_now_add=True)
	conteudo = models.TextField()
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class SolicitacaoEntrada(models.Model):
    from home.models import Campanha, Perfil
    de_usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='solicitacoes_enviadas_campanha')
    para_campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, related_name='solicitacoes_entrada')
    status = models.CharField(max_length=20, default='Pendente')

    def aceitar_solicitacao(self):
        self.status = 'Aceita'
        self.save()

        # Obtém a campanha associada à solicitação
        campanha = self.para_campanha

        # Obtém o grupo associado à campanha
        grupo = campanha.obter_grupo()

        if grupo:
            grupo.adicionar_usuario_ao_grupo(self.de_usuario.nomePerfil)

            # Adicione prints para verificar o fluxo
            print(f"Grupo associado à campanha: {grupo.uuid}")
            print(f"Usuário a ser adicionado: {self.de_usuario.nomePerfil}")
        else:
            # Adicione um print para indicar que a campanha não tem um grupo associado
            print(f"A campanha {campanha.nomeCampanha} não tem um grupo associado.")