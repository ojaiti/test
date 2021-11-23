from django.contrib import admin
from division.models import Division
# Register your models here.

@admin.register(Division)

class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'is_active', 'region']