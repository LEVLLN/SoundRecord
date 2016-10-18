from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
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
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return redirect('/welcome')
    else:
        # Отображение страницы с ошибкой
        return redirect('/')

def login_page(request):
    return render(request,'reservation/login.html')

def welcome_page(request):
    from django.contrib.auth.models import User
    username = request.user
    context = {
        'username': username,

    }
    return render(request, 'reservation/welcome_page.html', context)
