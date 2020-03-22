
from rest_framework import serializers
from .calculations import ZipAirCalculations
from django.conf import settings


class ZipAirplanesSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    passengers = serializers.IntegerField()
    tank_capacity = serializers.SerializerMethodField()
    per_passenger_consumption = serializers.SerializerMethodField()
    per_minute_fuel_consumption = serializers.SerializerMethodField()
    max_fly_minutes = serializers.SerializerMethodField()
    fuel_required = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'passengers', 'tank_capacity', 'fuel_consumption')

    def validate(self, data):
        airplane = ZipAirCalculations(data)
        if airplane.fuel_required > airplane.tank_capacity:
            raise serializers.ValidationError(
                'Plane cannot accept that much passengers.')
        return data

    def get_tank_capacity(self, obj):
        return ZipAirCalculations(obj).tank_capacity

    def get_per_passenger_consumption(self, obj):
        return ZipAirCalculations(obj).per_passenger_consumption

    def get_per_minute_fuel_consumption(self, obj):
        return ZipAirCalculations(obj).per_minute_fuel_consumption

    def get_max_fly_minutes(self, obj):
        return ZipAirCalculations(obj).max_fly_minutes

    def get_fuel_required(self, obj):
        return ZipAirCalculations(obj).fuel_required

class ZipAirlinesSerializer(serializers.Serializer):
    '''
    Serializer for all airplanes, with validation for max allowed planes.
    '''

    airplanes = ZipAirplanesSerializer(many=True)

    class Meta:
        fields = ('airplanes',)

    def validate_airplanes(self, value):
        if len(value) > settings.MAX_PLANES:
            raise serializers.ValidationError(
                'Max %s planes allowed.' % settings.MAX_PLANES)
        return value
