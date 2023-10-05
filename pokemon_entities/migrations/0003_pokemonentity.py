# Generated by Django 4.2.6 on 2023-10-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0002_pokemon_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="PokemonEntity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "longitude",
                    models.FloatField(blank=True, verbose_name="Долгота точки"),
                ),
                (
                    "latitude",
                    models.FloatField(blank=True, verbose_name="Широта точки"),
                ),
            ],
        ),
    ]
