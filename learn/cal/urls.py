from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.hello,name='hello'),
    # path('out',views.out,name='out'),
    path('temp',views.temp,name='temp')
]