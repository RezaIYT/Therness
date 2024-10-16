from django.urls import path
from api.views import calculate

urlpatterns = [
    path('calculate/', calculate.as_view(), name='calculate'),
]
