import os
from django.db import models
from home.models import Campanha
from meus_personagens.models import DnD, OrdemParanormal, Tormenta, CallOfCthulhu, Personagem
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class PastaCriaturas(models.Model):
    nome = models.CharField(max_length=100)
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)

class DnDCampanha(DnD):
    campanha_id = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    pasta = models.ForeignKey(PastaCriaturas, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        # Excluir tokens associados
        Token.objects.filter(content_type=ContentType.objects.get_for_model(self), object_id=self.id).delete()
        super().delete(*args, **kwargs)
        

class OrdemParanormalCampanha(OrdemParanormal):
    campanha_id = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    pasta = models.ForeignKey(PastaCriaturas, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        # Excluir tokens associados
        Token.objects.filter(content_type=ContentType.objects.get_for_model(self), object_id=self.id).delete()
        super().delete(*args, **kwargs)

class TormentaCampanha(Tormenta):
    campanha_id = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    pasta = models.ForeignKey(PastaCriaturas, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        # Excluir tokens associados
        Token.objects.filter(content_type=ContentType.objects.get_for_model(self), object_id=self.id).delete()
        super().delete(*args, **kwargs)

class CallOfCthulhuCampanha(CallOfCthulhu):
    campanha_id = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    pasta = models.ForeignKey(PastaCriaturas, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        # Excluir tokens associados
        Token.objects.filter(content_type=ContentType.objects.get_for_model(self), object_id=self.id).delete()
        super().delete(*args, **kwargs)
    
class Map(models.Model):
    name = models.CharField(max_length=100)
    campanha_id = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='maps/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Remover a imagem do mapa
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        
        # Excluir tokens associados e suas imagens
        for token in self.token_set.all():
            token.delete()  # Isso chama o método delete do Token, que remove a imagem
            
        # Excluir o mapa
        super().delete(*args, **kwargs)


class Token(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    
    # Campos para referenciar diferentes personagens
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    personagem = GenericForeignKey('content_type', 'object_id')
    
    image = models.ImageField(upload_to='tokens/')
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)

    def __str__(self):
        return f"Token on {self.map.name}"


