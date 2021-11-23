from django.db import models
from farms.models import Farm
# Create your models here.

class NightsCordoba(models.Model):
    farm_origen = models.OneToOneField(Farm, on_delete=models.CASCADE, default=None)
    tarara_s4 = models.PositiveSmallIntegerField(default=2)
    tarara_500 = models.PositiveSmallIntegerField(default=2)
    tarara_s2 = models.PositiveSmallIntegerField(default=2)
    tarara_km_11_s3 = models.PositiveSmallIntegerField(default=2)
    tarara_s5 = models.PositiveSmallIntegerField(default=2)
    tarara_2000 = models.PositiveSmallIntegerField(default=2)
    tarara_s3 = models.PositiveSmallIntegerField(default=2)
    

    class Meta:
        ordering = ('farm_origen',)
    def __str__(self):
        return f'{self.farm_origen}'