from django.db import models

class Game(models.Model):
    title = models.CharField("Game title", max_length=50, unique=True)
    description = models.TextField("Game description")
    designer = models.CharField("Game designer", max_length=50)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    est_time_to_play = models.DurationField()
    age_recommendation = models.IntegerField()
    player = models.ForeignKey("Player", verbose_name=("Player who created game entry"), on_delete=models.CASCADE)
    