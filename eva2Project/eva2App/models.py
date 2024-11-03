from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)

class Libro(models.Model):
    codigo = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    precio = models.IntegerField()
    n_paginas = models.IntegerField()
    stock = models.IntegerField()
    autor = models.ManyToManyField(Autor, related_name='libros')

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    edad = models.IntegerField()
    correo = models.EmailField()
    libros_comprados = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='clientes', null=True, blank=True)
    
