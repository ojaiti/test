from django.contrib import admin
from status_farm.models import StatusFarm
# Register your models here.
@admin.register(StatusFarm)

class StatusFarmAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']