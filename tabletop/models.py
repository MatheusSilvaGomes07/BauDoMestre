from django.db import models
from home.models import Campanha

class Map(models.Model):
    name = models.CharField(max_length=100)
    campanha_id = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='maps/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Token(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tokens/')
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)

    def __str__(self):
        return f"Token on {self.map.name}"
