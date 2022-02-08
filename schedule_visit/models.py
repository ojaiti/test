from django.db import models
from farms.models import Farm
from users.models import User
from status_authorization.models import StatusAuthorization
# Create your models here.
class ScheduleVisit(models.Model):
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    farm = models.ForeignKey(Farm, on_delete=models.SET_NULL, null=True, blank=True)
    nights = models.PositiveSmallIntegerField(null=False)
    number_of_people = models.PositiveSmallIntegerField(null=False)
    reason = models.TextField(max_length=255)
    status_aut = models.ForeignKey(StatusAuthorization, on_delete=models.SET_NULL, null=True, blank=True)
    is_authorized = models.BooleanField(default=False)
    user_sol = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_sol")
    user_auth = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_auth")

    def save(self, *args, **kwargs):
        print('Guardado')
        #Si el usuario ya tiene una  visita agendada no puede agregar otra el mismo dia