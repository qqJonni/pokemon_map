# Generated by Django 4.2.6 on 2023-10-07 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0010_pokemon_title_en_pokemon_title_jp"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="previous_evolution",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="next_evolutions",
                to="pokemon_entities.pokemon",
                verbose_name="Из кого эволюционирует",
            ),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="defence",
            field=models.IntegerField(verbose_name="Защита:"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="health",
            field=models.IntegerField(verbose_name="Здоровье:"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="level",
            field=models.IntegerField(verbose_name="Уровень:"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="stamina",
            field=models.IntegerField(verbose_name="Выносливость:"),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="strength",
            field=models.IntegerField(verbose_name="Атака:"),
        ),
    ]
