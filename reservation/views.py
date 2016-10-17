from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
# Create your views here.
from reservation.models import Schedule, Reservation


def home(request):
    schedules = Reservation.objects.all()
    context ={
        'schedules': schedules,
    }

    return render(request, 'reservation/home.html',context)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect("reservation/home.html")
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")

def loginpage(request):
    return render(request,'reservation/login.html')