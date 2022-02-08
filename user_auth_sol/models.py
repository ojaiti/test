from django.db import models
from users.models import User
# Create your models here.
class UserAuthSol(models.Model):
    user_auth_visit = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="user_auth_visit")
    user_sol_visist = models.ManyToManyField(User, related_name="user_sol_visit")

    def get_users_sol(self):
        return ",".join([str(u) for u in self.user_sol_visist.all()])

    def __unicode__(self):
        return "{0}".format(self.user_auth_visit)
