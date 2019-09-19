from rest_framework import serializers
from .models import *

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'id',
            'type',
            'address',
            'Latitude',
            'Longitude',
            'radius_soundcover',
            'activity'
        )