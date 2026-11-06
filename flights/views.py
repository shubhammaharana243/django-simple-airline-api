from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Flight
from .serializers import FlightSerializer

# Create your views here.

class FlightViewSets(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

