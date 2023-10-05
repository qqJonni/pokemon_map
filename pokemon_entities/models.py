from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=128, verbose_name='Pokemon name')
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    title = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Pokemon name')
    longitude = models.FloatField(verbose_name="Долгота точки")
    latitude = models.FloatField(verbose_name="Широта точки")
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(max_length=12, default=1)
    health = models.IntegerField(max_length=12, default=10)
    strength = models.IntegerField(max_length=12, default=5)
    defence = models.IntegerField(max_length=12, default=5)
    stamina = models.IntegerField(max_length=12, default=5)
