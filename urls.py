from django.urls import path
from api.views import calculate
from django.contrib import admin

urlpatterns = [
    path('calculate/', calculate.as_view(), name='calculate'),
]
