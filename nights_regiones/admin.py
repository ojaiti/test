from django.contrib import admin
from nights_regiones.models import NightsRegiones
# Register your models here.

@admin.register(NightsRegiones)

class NightsRegionesAdmin(admin.ModelAdmin):
    list_display = ['noroeste','veracruz','tehuacan','cordoba']
