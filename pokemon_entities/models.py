from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=128, verbose_name='Pokemon name')
    title_en = models.CharField(max_length=128, verbose_name='Pokemon English name')
    title_jp = models.CharField(max_length=128, verbose_name='Pokemon Japan name')
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField(verbose_name='Pokemon description', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    title = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Pokemon name')
    longitude = models.FloatField(verbose_name="Долгота точки")
    latitude = models.FloatField(verbose_name="Широта точки")
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=10)
    strength = models.IntegerField(default=5)
    defence = models.IntegerField(default=5)
    stamina = models.IntegerField(default=5)


