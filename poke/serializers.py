from rest_framework import serializers
from .models import PokemonModel


class PokeModelSerializer(serializers.ModelSerializer):
    player = serializers.CharField(max_length=100, source='custumer.username')

    class Meta:
        model = PokemonModel
        fields = ('player', 'pokemon')
