from django.urls import path
from .views import GetTemperature,GetTempMode,GetUss


urlpatterns = [
    path('temperature/',GetTemperature.as_view()),
    path('tempe-mode/',GetTempMode.as_view()),
    path('uss/',GetUss.as_view())
]