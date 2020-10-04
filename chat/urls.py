from django.contrib import admin
from django.urls import path
from .views import list, read

urlpatterns = [
    path('list', list),
    path('read', read)
]
