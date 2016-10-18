from django.conf.urls import url
from reservation import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/', views.Registration.register, name='register'),
    url(r'^login/', views.Authorization.login, name='login'),
    url(r'^logout/', views.Authorization.logout, name='logout')
]
