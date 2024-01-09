from django.shortcuts import render
import random


from .serializers import TemperatureSerializer,TempModeSerializer,UssSerializer,IotSerializer
from .models import temperatureModel,tempModeModel,UssModel,IotModel
from rest_framework.response import Response
from rest_framework.views import APIView

class GetIot(APIView):
    def get(self, request):
        data = list(IotModel.objects.all())
        random.shuffle(data)
        serializer = IotSerializer(data[:1], many=True)
        return Response(serializer.data)

class GetTemperature(APIView):
    def get(self, request):
    
        data = list(temperatureModel.objects.all())
        random.shuffle(data)
        serializer = TemperatureSerializer(data[:1], many=True)
        return Response(serializer.data)
    
class GetTempMode(APIView):
    def get(self, request):
        data = list(tempModeModel.objects.all())
        random.shuffle(data)
        serializer = TempModeSerializer(data[:1], many=True)
        return Response(serializer.data)
    

class GetUss(APIView):
    def get(self, request):
        data = list(UssModel.objects.all())
        random.shuffle(data)
        serializer = UssSerializer(data[:1], many=True)
        return Response(serializer.data)