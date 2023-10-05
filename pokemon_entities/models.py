from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=128, verbose_name='Pokemon name')
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    longitude = models.FloatField(verbose_name="Долгота точки", blank=True)
    latitude = models.FloatField(verbose_name="Широта точки", blank=True)
    title = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Pokemon name')
