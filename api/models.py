from django.db import models

class tempModeModel(models.Model):
    tempMode = models.CharField(max_length=4)

    def __str__(self):
        return self.tempMode
    
class temperatureModel(models.Model):
    temperature = models.CharField(max_length=4)

    def __str__(self):
        return self.temperature
    
class UssModel(models.Model):
    uss = models.CharField(max_length=4)

    def __str__(self):
        return self.uss