from rest_framework import serializers
from .models import IotModel



class IotSerializer(serializers.ModelSerializer):
    class Meta:
        model = IotModel
        fields = ['id','temperature_iot','temp_mode_iot','uss_iot']