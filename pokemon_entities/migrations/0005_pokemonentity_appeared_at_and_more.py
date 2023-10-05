# Generated by Django 4.2.6 on 2023-10-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0004_pokemonentity_title_alter_pokemon_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateTimeField(null=True),
        ),
    ]
