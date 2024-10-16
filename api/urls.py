from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculate, name='calculate'),  # Register the calculate URL
]
