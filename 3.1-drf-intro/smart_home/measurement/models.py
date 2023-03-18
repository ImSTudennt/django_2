from django.db import models
from django.forms.fields import ImageField




class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', null=True)
    nullable = models.ImageField(null=True)


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
