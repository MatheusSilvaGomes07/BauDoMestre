from django.db import models
from django.conf import settings
from django.utils import timezone

class ListaAmigos(models.Model):

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user")
    amigos = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="amigos")

    def __str__(self):
        return self.user.username
    
    def add_amigo(self, user):

        if not user in self.amigos.all():
            self.amigos.add(user)
            self.save()

    def remover_amigo(self, user):

        if user in self.friends.all():
            self.amigos.remove(user)

    def desfazer_amizade(self, removee):

        remover_lista_amigos = self

        remover_lista_amigos.remover_amigo(removee)

        lista_amigos = ListaAmigos.objects.get(usuario=removee)
        lista_amigos.remover_amigo(self.user)

    def mutuo(self, amigo):

        if amigo in self.amigos.all():
            return True
        return False
    
class PedidoDeAmizade(models.Model):

    remetente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="remetente")
    recebedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="recebedor")

    esta_ativo = models.BooleanField(blank=True, null=False, default=True)

    tempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remetente.username
    
    def aceitar(self):

        lista_recebedor = ListaAmigos.objects.get(usuario=self.recebedor)

        if lista_recebedor:
            lista_recebedor.add_amigo(self.remetente)
            lista_remetente = ListaAmigos.objects.get(usuario=self.remetente)

            if lista_remetente:
                lista_remetente.add_amigo(self.recebedor)
                self.esta_ativo = False
                self.save()

    def recusar(self):

        self.esta_ativo = False
        self.save()

    def cancelar(self):

        self.esta_ativo