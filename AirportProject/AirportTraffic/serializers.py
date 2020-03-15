from rest_framework import serializers
from .models import AirportModel

...
class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirportModel
        fields = ('primary_key','report_period','terminal', 'arrival_departure', 'domestic_international', 'passenger_count')