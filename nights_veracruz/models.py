from django.db import models
from farms.models import Farm
# Create your models here.
class NightsVeracruz(models.Model):
    farm_origen = models.OneToOneField(Farm, on_delete=models.CASCADE, default=None)
    iguazu = models.PositiveSmallIntegerField(default=2)
    mata_espino = models.PositiveSmallIntegerField(default=2)
    gertrudis = models.PositiveSmallIntegerField(default=2)
    capulines_1 = models.PositiveSmallIntegerField(default=2)
    angelito = models.PositiveSmallIntegerField(default=2)
    capulines_2 = models.PositiveSmallIntegerField(default=2)
    palomas = models.PositiveSmallIntegerField(default=2)
    milagro = models.PositiveSmallIntegerField(default=2)
    capulines_rentado = models.PositiveSmallIntegerField(default=2)
    cuarentena = models.PositiveSmallIntegerField(default=2)
    gloria = models.PositiveSmallIntegerField(default=2)
    cruz = models.PositiveSmallIntegerField(default=2)
    gregorio = models.PositiveSmallIntegerField(default=2)
    copital = models.PositiveSmallIntegerField(default=2)
    cuarentena_lupita = models.PositiveSmallIntegerField(default=2)
    oficina_angelito = models.PositiveSmallIntegerField(default=2)
    almacen_general = models.PositiveSmallIntegerField(default=2)
    planta_alimentos = models.PositiveSmallIntegerField(default=2)
    venta_deposito = models.PositiveSmallIntegerField(default=2)
   

    class Meta:
        ordering = ('farm_origen',)
        #para ordenear la columna

    def __str__(self):
        return f'{self.farm_origen}'