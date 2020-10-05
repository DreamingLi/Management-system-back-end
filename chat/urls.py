from django.contrib import admin
from django.urls import path
from .views import listMsg, read

urlpatterns = [
    path('listMsg', listMsg),
    path('read', read)
]
