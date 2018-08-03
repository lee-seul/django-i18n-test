# coding: utf-8

from django.urls import path

from .views import hello

app_name = 'translation'
urlpatterns = [
    path('hello', hello, name='hello'),
]
