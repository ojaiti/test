from django.contrib import admin
from nights_tehuacan.models import NightsTehuacan
# Register your models here.

@admin.register(NightsTehuacan)

class NightsTehuacanAdmin(admin.ModelAdmin):
    list_display = ['farm_origen','pazoltepec_1a','pazoltepec_1b','san_luis_1c','san_luis_2b','cacaluapan_2c','cuarentena_mora','san_luis_3b','cacaluapan_3c','tepanco_3a','tepanco_3b','tepanco_3c','recria_san_bartolo','oficina_generales','almacen_general','planta_alimentos']

