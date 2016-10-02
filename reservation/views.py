from django.shortcuts import render

# Create your views here.
from reservation.models import Schedule


def home(request):
    schedules = Schedule.objects.all()
    context ={
        'schedules': schedules,
    }
    return render(request, 'reservation/home.html',context)

