from django.urls import path
from api.views import CalculationView

urlpatterns = [
    path('calculate/', CalculationView.as_view(), name='calculate'),
]
