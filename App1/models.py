from django.db import models

# Create your models here.

class Familiar(models.model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    nacimiento=models.DateField()

class Mascota(models.model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    nacimiento=models.DateField()

class Vehiculo(models.modell):
    marca=models.CharField(max_length=50)
    año=models.IntegerField()