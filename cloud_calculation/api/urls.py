from django.urls import path
from . import views

print("Hello")
print(views.calculate)

urlpatterns = [
    path('calculate/', views.calculate, name=['calculate']),  # Register the calculate URL
]
