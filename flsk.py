

from flask import Flask, request, jsonify
import numpy as np 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import uvicorn
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from django.urls import path




class MultiplyView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            value = data.get('value')
            if value is None:
                return JsonResponse({'error': 'No value provided'}, status=400)
            
            result = np.array([10, 20, 30]) * value
            return JsonResponse({'result': result.tolist()})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

urlpatterns = [
    path('multiply/', MultiplyView.as_view(), name='multiply')
]




