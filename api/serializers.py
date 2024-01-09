from rest_framework import serializers
from .models import tempModeModel, temperatureModel,UssModel,IotModel

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

class IotSerializer(serializers.ModelSerializer):
    class Meta:
        model = IotModel
        fields = ['id','temperature_iot','temp_mode_iot','uss_iot']