from django.conf.urls import url
from reservation.views import home
from reservation.views import loginpage
from reservation.views import login
urlpatterns = [
    url(r'^$', home, name='home'),
    # url(r'^login/$', loginpage, name='login'),
    url(r'^login/$', login, name='login')
    ]