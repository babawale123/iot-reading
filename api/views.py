from django.shortcuts import render
import random


from .serializers import IotSerializer
from .models import IotModel
from rest_framework.response import Response
from rest_framework.views import APIView

class GetIot(APIView):
    def get(self, request):
        data = list(IotModel.objects.all())
        random.shuffle(data)
        serializer = IotSerializer(data[:1], many=True)
        return Response(serializer.data)


