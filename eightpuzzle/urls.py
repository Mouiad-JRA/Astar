from django.contrib import admin
from django.urls import path

from eightpuzzle.views import index

app_name = 'eightpuzzle'
urlpatterns = [
    path('', index, name='a_star'),
]
