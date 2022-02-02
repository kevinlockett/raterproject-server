from django.db import models

class Category(models.Model):
    name = models.CharField("game type", max_length=50)