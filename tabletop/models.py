# models.py
from django.db import models

class Object(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='objects/', null=True, blank=True)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)