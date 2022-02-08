from django.db import models
from users.models import User
from farms.models import Farm
# Create your models here.
class VisitedFarmByUser(models.Model):
    user = models.ForeignKey(User, related_name='user', null=True,on_delete=models.SET_NULL)
    origin_farm = models.ForeignKey(Farm, related_name='origin_farm', null=True, on_delete=models.SET_NULL)
    destination_farm = models.ForeignKey(Farm, related_name='destination_farm',null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    is_same_flow = models.BooleanField(default=False)
    nights = models.PositiveSmallIntegerField(default=0)
    number_of_people = models.PositiveSmallIntegerField(null=False)
    names_of_people = models.TextField(null=False, blank=True)
    reason = models.TextField(max_length=250, null=True)
    is_authorized = models.BooleanField(default=False)
    authorizing_user = models.ForeignKey(User, null=True, blank=True, related_name='authorizing_user', on_delete=models.SET_NULL)

    def __str__(self):
        return f'granja visitada por {self.user}'