from django.contrib import admin
from status_authorization.models import StatusAuthorization
# Register your models here.
@admin.register(StatusAuthorization)

class StatusAuthorizationAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']