from django.db import models

class Category(models.Model):
    label = models.CharField("game type", max_length=50)