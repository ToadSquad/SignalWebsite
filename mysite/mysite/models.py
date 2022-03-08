from django.db import models

# Create your models here.
class triggerData(models.Model):
    symbol = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    ratio = models.CharField(max_length=30)
    upper = models.CharField(max_length=30)
    lower = models.CharField(max_length=30)
    time = models.DateTimeField()
    priceEntered = models.CharField(max_length=30)
    currentPL = models.CharField(max_length=30)
    profit = models.CharField(max_length=30)

class patternData(models.Model):
    symbol = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    pattern = models.CharField(max_length=30)
    time = models.DateTimeField()
