from django.contrib import admin
from django.urls import path
from .views import register, login, update,list

urlpatterns = [
    path('register', register),
    path('login', login),
    path('update', update),
    path('list',list)
]
