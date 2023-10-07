from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=128, verbose_name='Pokemon name')
    title_en = models.CharField(max_length=128, verbose_name='Pokemon English name', blank=True)
    title_jp = models.CharField(max_length=128, verbose_name='Pokemon Japan name', blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField(verbose_name='Pokemon description')
    previous_evolution = models.ForeignKey("Pokemon", on_delete=models.CASCADE, blank=True, null=True,
                                           verbose_name="Из кого эволюционирует", related_name='next_evolutions')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Pokemon name',
                                related_name='pokemon_entitys')
    longitude = models.FloatField(verbose_name="Долгота точки")
    latitude = models.FloatField(verbose_name="Широта точки")
    appeared_at = models.DateTimeField(verbose_name="Появится в:", blank=True)
    disappeared_at = models.DateTimeField(verbose_name="Исчезнет в:", blank=True)
    level = models.IntegerField(verbose_name="Уровень:")
    health = models.IntegerField(verbose_name="Здоровье:")
    strength = models.IntegerField(verbose_name="Атака:")
    defence = models.IntegerField(verbose_name="Защита:")
    stamina = models.IntegerField(verbose_name="Выносливость:")
