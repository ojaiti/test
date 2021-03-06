from django.contrib import admin
from visitedfarmbyuser.models import VisitedFarmByUser
# Register your models here.

@admin.register(VisitedFarmByUser)
class VisitedFarmByUserAdmin(admin.ModelAdmin):
    list_display= ['user','origin_farm','destination_farm','date','is_same_flow','nights','number_of_people', 'names_of_people','reason', 'is_authorized','authorizing_user']
