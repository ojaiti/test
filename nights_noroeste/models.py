from django.db import models
from farms.models import Farm
# Create your models here.

class NightsNoroeste(models.Model):
    farm_origen = models.OneToOneField(Farm, on_delete=models.CASCADE, default=None)
    is_active = models.BooleanField(default=1, null=True, blank=True)
    tpp_s1 = models.PositiveSmallIntegerField(default=2)
    xaratanga_1 = models.PositiveSmallIntegerField(default=2)
    ctg_xaratanga = models.PositiveSmallIntegerField(default=2)
    porcina_3 = models.PositiveSmallIntegerField(default=2)
    porcina_4_5 = models.PositiveSmallIntegerField(default=2)
    tpp_3_0_1 = models.PositiveSmallIntegerField(default=2)
    tpp_3_0_2 = models.PositiveSmallIntegerField(default=2)
    tpp_3_0_3 = models.PositiveSmallIntegerField(default=2)
    tpp_3_0_4 = models.PositiveSmallIntegerField(default=2)
    tpp_3_0_5 = models.PositiveSmallIntegerField(default=2)
    xaratanga_s2 = models.PositiveSmallIntegerField(default=2)
    xaratanga_cmg = models.PositiveSmallIntegerField(default=2)
    seccion_10 = models.PositiveSmallIntegerField(default=2)
    porcina_9 = models.PositiveSmallIntegerField(default=2)
    laguna_1 = models.PositiveSmallIntegerField(default=2)
    laguna_2 = models.PositiveSmallIntegerField(default=2)
    querobabi = models.PositiveSmallIntegerField(default=2)
    porcina_6 = models.PositiveSmallIntegerField(default=2)
    porcina_1 = models.PositiveSmallIntegerField(default=2)
    seccion_2 = models.PositiveSmallIntegerField(default=2)
    porcina_2 = models.PositiveSmallIntegerField(default=2)
    porcina_7 = models.PositiveSmallIntegerField(default=2)
    luis_emilio = models.PositiveSmallIntegerField(default=2)
    maria_emma = models.PositiveSmallIntegerField(default=2)
    ludi = models.PositiveSmallIntegerField(default=2)
    porcina_10 = models.PositiveSmallIntegerField(default=2)
    elsa = models.PositiveSmallIntegerField(default=2)
    la_palma = models.PositiveSmallIntegerField(default=2)
    guaymita = models.PositiveSmallIntegerField(default=2)
    xaratanga_3 = models.PositiveSmallIntegerField(default=2)
    c_mezquite = models.PositiveSmallIntegerField(default=2)
    c_obregon = models.PositiveSmallIntegerField(default=2)
    c_huatabampo = models.PositiveSmallIntegerField(default=2)
    oficina_generales = models.PositiveSmallIntegerField(default=2)
    almacen_general = models.PositiveSmallIntegerField(default=2)
    planta_alimentos = models.PositiveSmallIntegerField(default=2)
    plata_tif_227 = models.PositiveSmallIntegerField(default=2)
    venta_resaga = models.PositiveSmallIntegerField(default=2)

    class Meta:
        pass
        #ordering = ('farm_origen',)
    def __str__(self):
        return f'{self.farm_origen}'