from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime

# Create your models here.
class Pasta(models.Model):
    nome = models.CharField(max_length=250)
    divisao = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        # Exclua todas as imagens associadas
        for arqui in self.arquivos.all():
            arquivo_path = arqui.file.path
            if os.path.exists(arquivo_path):
                os.remove(arquivo_path)
        super().delete(*args, **kwargs)

class File(models.Model):
    nome = models.CharField(max_length=250)
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE, related_name='arquivos')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    data = models.CharField(max_length=10, default=datetime.now().strftime('%d/%m/%Y'))

    def delete(self, *args, **kwargs):
        # Exclua todas as imagens associadas
        arquivo_path = self.file.path
        if os.path.exists(arquivo_path):
            os.remove(arquivo_path)
        super().delete(*args, **kwargs)
