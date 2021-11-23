from django.contrib import admin
from nights_cordoba.models import NightsCordoba
# Register your models here.
@admin.register(NightsCordoba)

class NightsCordobaAdmin(admin.ModelAdmin):
    list_display = ['farm_origen','tarara_s4','tarara_500','tarara_s2','tarara_km_11_s3','tarara_s5','tarara_2000','tarara_s3']

    