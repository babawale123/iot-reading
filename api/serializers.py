from rest_framework import serializers
from .models import tempModeModel, temperatureModel,UssModel

class TempModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = tempModeModel
        fields = ['id', 'tempMode']

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperatureModel
        fields = ['id', 'temperature']

class UssSerializer(serializers.ModelSerializer):
    class Meta:
        model = UssModel
        fields = ['id', 'uss']