from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

# Create your views here.

class FlightViewSets(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSets(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

