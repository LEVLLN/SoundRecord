from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #dff
    url(r'^admin/', admin.site.urls),
    url(r'^', include('reservation.urls')),

]
