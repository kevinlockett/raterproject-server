from django.db import models

class Review(models.Model):
    review = models.TextField("Game review")
    player = models.ForeignKey("Player", verbose_name=("Player who wrote review"), on_delete=models.CASCADE)
    game = models.ForeignKey("Game", verbose_name=("Game being reviewed"), on_delete=models.CASCADE)