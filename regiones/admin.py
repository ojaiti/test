from django.contrib import admin
from regiones.models import Regiones
# Register your models here.
@admin.register(Regiones)

class RegionesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'is_active']