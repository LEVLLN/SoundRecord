from django.conf.urls import url
from reservation.views import home
urlpatterns = [
    url(r'^$', home, name='home'),
    ]