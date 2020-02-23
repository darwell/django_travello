from django.urls import path

from . import views

urlpatterns = [
    path('', views.travello, name='home'),
    path('destination', views.destination, name='destination')
]
