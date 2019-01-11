from django.db import models

# Create your models here
class Weather(models.Model):
    measured = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=250)
    temperature = models.FloatField()
    photo = models.URLField()
    currentcondition = models.CharField(max_length=250)

# 401: Create a model for forecasts

