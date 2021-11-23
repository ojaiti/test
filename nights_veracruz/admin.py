from django.contrib import admin
from nights_veracruz.models import NightsVeracruz
# Register your models here.

@admin.register(NightsVeracruz)

class NightsVeracruzAdmin(admin.ModelAdmin):
    list_display = ['farm_origen','iguazu','mata_espino','gertrudis','capulines_1','angelito','capulines_2','palomas','milagro','capulines_rentado','cuarentena','gloria','cruz','gregorio','copital','cuarentena_lupita','oficina_angelito','almacen_general','planta_alimentos','venta_deposito']

