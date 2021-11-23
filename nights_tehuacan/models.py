from django.db import models
from farms.models import Farm
# Create your models here.
class NightsTehuacan(models.Model):
    farm_origen = models.OneToOneField(Farm, on_delete=models.CASCADE, default=None)
    pazoltepec_1a = models.PositiveSmallIntegerField(default=2)
    pazoltepec_1b = models.PositiveSmallIntegerField(default=2)
    san_luis_1c = models.PositiveSmallIntegerField(default=2)
    san_luis_2b = models.PositiveSmallIntegerField(default=2)
    cacaluapan_2c = models.PositiveSmallIntegerField(default=2)
    cuarentena_mora = models.PositiveSmallIntegerField(default=2)
    san_luis_3b = models.PositiveSmallIntegerField(default=2)
    cacaluapan_3c = models.PositiveSmallIntegerField(default=2)
    tepanco_3a = models.PositiveSmallIntegerField(default=2)
    tepanco_3b = models.PositiveSmallIntegerField(default=2)
    tepanco_3c = models.PositiveSmallIntegerField(default=2)
    recria_san_bartolo = models.PositiveSmallIntegerField(default=2)
    oficina_generales = models.PositiveSmallIntegerField(default=2)
    almacen_general = models.PositiveSmallIntegerField(default=2)
    planta_alimentos = models.PositiveSmallIntegerField(default=2)
    

    """ class Meta:
        ordering = ('farm_origen',) #ordenamiento"""

    def __str__(self):
        return f'{self.farm_origen}'