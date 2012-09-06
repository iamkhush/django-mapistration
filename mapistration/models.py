from django.db import models


class Place(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
