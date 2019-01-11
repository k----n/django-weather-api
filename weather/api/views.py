from django.shortcuts import render

from rest_framework import viewsets
from .models import Weather
from .serializers import WeatherSerializer

# Create your views here.
class WeatherView(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    allowed_methods = ['GET', 'POST']

