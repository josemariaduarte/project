

from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    #codigo = models.AutoField(primary_key= True)
    #django te crea un id autoincrementable.

    nombre = models.CharField(max_length=50)
    habilitado = models.BooleanField(default = True)

    class Meta:
        verbose_name_plural = "nacionalidades"
class Persona(models.Model):
    nombre = models.CharField(max_length=50)

class Animal(models.Model):
    nombre = models.CharField(max_length=50)