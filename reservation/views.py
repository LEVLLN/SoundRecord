from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from reservation.models import Schedule
from django.contrib.auth.models import User


def home(request):
    schedules = Schedule.objects.all()
    context = {
        'schedules': schedules,
    }
    return render(request, 'reservation/home.html', context)


class Authorization:
    def login(request):
        if request.method == "GET":
            if request.user.is_authenticated():
                return HttpResponse("You are authorized")
            else:
                return render(request, "registration/login.html")
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse("its ok")
            else:
                return HttpResponse("No users like this")

    def logout(request):
        auth.logout(request)
        return HttpResponseRedirect("/login")


class Registration:
    def register(request):
        if request.user.is_authenticated():
                return HttpResponse("You are authorized")
        else:
            if request.method == "GET":
                return render(request, "registration/register.html")
            if request.method == "POST":
                try:
                    username = request.POST['username']
                    password = request.POST['password']
                    email = request.POST['email']
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    if user is not None and user.is_active:
                        return HttpResponse("The registration has been completed succsesfully")
                except Exception:
                    return HttpResponse("FAIL")
