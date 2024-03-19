from django.db import models

class Map(models.Model):
    name = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='maps/', null=True, blank=True)

class Token(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tokens/')
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
