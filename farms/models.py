from django.db import models
from regiones.models import Regiones
from status_farm.models import StatusFarm
from django.core.exceptions import ValidationError
# Create your models here.
class Farm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    id_ref = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(StatusFarm, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Regiones, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.name}'
    def save(self, *args, **kwargs):
        print('hello')
        self.id_ref += 1
        super(Farm, self).save(*args, **kwargs)
  
                
               

