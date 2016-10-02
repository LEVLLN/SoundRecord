from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Schedule(models.Model):
    soundman = models.ForeignKey(User)
    start_of_the_day = models.TimeField()
    end_of_the_day = models.TimeField()
    working_day = models.IntegerField()


class Reservation(models.Model):
    reservation_user = models.ForeignKey(User)
    reservation_sound_man = Schedule.soundman
    is_active = models.BooleanField(default=True)
    start = models.DateTimeField()
    duration = models.DecimalField(max_digits=20,decimal_places=10)





