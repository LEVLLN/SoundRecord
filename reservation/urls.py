from django.conf.urls import url
from reservation.views import home
from reservation.views import login_page
from reservation.views import login
from reservation.views import welcome_page

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^accept/$', login_page, name='logaccept'),
    url(r'^login', login, name='login'),
    url(r'^welcome', welcome_page, name='welcome')
]
