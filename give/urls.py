from django.contrib import admin
from django.urls import path
from . import views as give_views

urlpatterns = [
    path('give/', give_views.give, name='give'),
    path('charge/', give_views.charge, name='charge'),
]
