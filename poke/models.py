from django.db import models
from django.contrib.auth.models import User


class PokemonModel(models.Model):
    custumer = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.CharField(verbose_name='Pokemon', max_length=100, default='')
    pokemon_url = models.CharField(verbose_name='Pokemon_url', unique=True,
                                   max_length=100, default='')
