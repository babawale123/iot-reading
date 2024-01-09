from django.db import models


    
class IotModel(models.Model):
    temperature_iot = models.CharField(max_length=7)
    temp_mode_iot = models.CharField(max_length=7)
    uss_iot = models.CharField(max_length=7)

    def __str__(self):
        return self.temperature_iot