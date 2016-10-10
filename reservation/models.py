from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.forms import DurationField


class Schedule(models.Model):
    soundman = models.ForeignKey(User)
    start_of_the_day = models.TimeField()
    end_of_the_day = models.TimeField()
    working_day = models.IntegerField()


class Reservation(models.Model):
    reservation_user = models.ForeignKey(User)
    reservation_sound_man = Schedule.soundman
    STATUS = (
        (1,'Active'),
        (2,'In progress'),
        (3,'Inactive')
    )
    is_active = models.IntegerField(choices=STATUS)
    start = models.DateTimeField()
    duration = DurationField()





