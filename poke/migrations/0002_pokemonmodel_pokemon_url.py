# Generated by Django 3.2.5 on 2021-07-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonmodel',
            name='pokemon_url',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Pokemon_url'),
        ),
    ]