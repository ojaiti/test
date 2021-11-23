from django.db import models
from farms.models import Farm
# Create your models here.
class NightsRegiones(models.Model):
    farm_origen = models.OneToOneField(Farm, on_delete=models.CASCADE, default=None)
    noroeste = models.PositiveSmallIntegerField(default=4)
    veracruz = models.PositiveSmallIntegerField(default=4)
    tehuacan = models.PositiveSmallIntegerField(default=4)
    cordoba = models.PositiveSmallIntegerField(default=4)

    class Meta:
        ordering = ('farm_origen',)

    def __str__(self):
        return f'{self.farm_origen}'