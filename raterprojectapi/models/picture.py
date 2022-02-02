from django.db import models

class Picture(models.Model):    
    image = models.ImageField(upload_to=None) 
    game = models.ForeignKey("Game", verbose_name=("Game being played"), on_delete=models.CASCADE)
    player = models.ForeignKey("Player", verbose_name=("Player who shared picture"), on_delete=models.CASCADE)