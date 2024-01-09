from django.urls import path
from .views import GetIot


urlpatterns = [
    path('iot-readings/',GetIot.as_view()),
]