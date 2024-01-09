from django.contrib import admin
from .models import temperatureModel,tempModeModel,UssModel

admin.site.register((temperatureModel,tempModeModel,UssModel))