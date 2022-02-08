from django.contrib import admin
from schedule_visit.models import ScheduleVisit
# Register your models here.
@admin.register(ScheduleVisit)
class ScheduleVisitAdmin(admin.ModelAdmin):
    list_display = ['start_date','end_date','farm','nights','number_of_people','reason','is_authorized','user_sol','user_auth',]

