from django.core.signals import request_finished, pre_save
from django.dispatch import receiver
from schedule_visit.models import ScheduleVisit

#@receiver(request_finished)
@receiver(pre_save, sender=ScheduleVisit)
def my_callback(sender, **kwargs):
    print("Request finished!")