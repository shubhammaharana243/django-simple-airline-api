from rest_framework import serializers
from .models import Flight, Airport


class FlightSerializer(serializers.ModelSerializer):
    origin = serializers.SlugRelatedField(
        queryset=Airport.objects.all(),
        slug_field='city'
    )

    destination = serializers.SlugRelatedField(
        queryset=Airport.objects.all(),
        slug_field='city'
    )

    class Meta:
        model = Flight
        fields = '__all__'