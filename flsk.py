

import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from django.urls import path


class CalculateView(View):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            value = data.get('value')
            if value is not None:
                result = value * np.array([10, 20, 30])  # Example calculation
                return JsonResponse({"result": result.tolist()})
            else:
                return JsonResponse({"detail": "No value provided"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid JSON"}, status=400)

# In your urls.py

urlpatterns = [
    path('calculate/', CalculateView.as_view(), name='calculate'),
]




