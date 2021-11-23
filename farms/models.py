from django.db import models
from regiones.models import Regiones
from division.models import Division
from status_farm.models import StatusFarm
# Create your models here.
class Farm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(StatusFarm, on_delete=models.SET_NULL, null=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Regiones, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'
