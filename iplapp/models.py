from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length = 50)
    owner = models.CharField(max_length = 64)
    home_city = models.CharField(max_length = 64)
