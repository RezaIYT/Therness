from django.urls import path
from api.views import calculate
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/', calculate.as_view(), name='calculate'),
]
