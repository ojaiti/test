from django.db import models
from regiones.models import Regiones
# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    region = models.ForeignKey(Regiones, on_delete=models.CASCADE)

    def __str__(self):
        return self.name