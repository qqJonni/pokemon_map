# Generated by Django 4.2.6 on 2023-10-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0008_pokemon_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="description",
            field=models.TextField(blank=True, verbose_name="Pokemon description"),
        ),
    ]
