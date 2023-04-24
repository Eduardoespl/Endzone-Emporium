from django.db import models

# Create your models here.
class cleats(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    marca = models.CharField(max_length=50, blank=False, default=None)
    modelo = models.CharField(max_length=100, blank=False, default=None)
    precio=models.FloatField(blank=False, default=None)
    talla = models.CharField(max_length=50, blank=False, default=None)

class cascos(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    marca = models.CharField(max_length=50, blank=False, default=None)
    modelo = models.CharField(max_length=100, blank=False, default=None)
    precio=models.FloatField(blank=False, default=None)
    talla = models.CharField(max_length=50, blank=False, default=None)

class accesorios(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    marca = models.CharField(max_length=50, blank=False, default=None)
    modelo = models.CharField(max_length=100, blank=False, default=None)
    precio=models.FloatField(blank=False, default=None)
    talla = models.CharField(max_length=50, blank=False, default=None)