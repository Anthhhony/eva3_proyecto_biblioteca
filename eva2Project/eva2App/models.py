from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    edad = models.IntegerField()
    correo = models.EmailField()

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)

# Create your models here.
