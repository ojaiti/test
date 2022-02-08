from django.contrib import admin
from farms.models import Farm
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.shortcuts import render
from django import forms
# Register your models here.

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class FarmResources(resources.ModelResource):
    fields = ('name',)

    class Meta:
        model = Farm

@admin.register(Farm)
class FarmAdmin(ImportExportModelAdmin):
    resource_class = FarmResources
    list_display = ['name','id_ref','created_at', 'status', 'is_active', 'region']
    import_id_fields = ('quarantine_nights',)
    #filter_horizontal = ['region']
    #search_fields = ['name'] buscador por nombre granjas




    

