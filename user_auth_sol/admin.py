from django.contrib import admin
from user_auth_sol.models import UserAuthSol
# Register your models here.
@admin.register(UserAuthSol)

class UserAuthSolAdmin(admin.ModelAdmin):
    list_display = ['user_auth_visit', 'get_users_sol'] #get_users_sol, es una funcion que esta en el archivo models

    