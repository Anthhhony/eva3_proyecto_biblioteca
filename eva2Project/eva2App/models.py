from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, EmailValidator, RegexValidator

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField(
        validators=[EmailValidator('El correo ingresado no es válido, compruebe el ejemplo: correoejemplo@gmail.com')]
    )

class Libro(models.Model):
    codigo = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    n_paginas = models.IntegerField(
        validators=[MinValueValidator(49)]
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    autor = models.ManyToManyField(Autor, related_name='libros')

class Cliente(models.Model):
    rut = models.CharField(
        max_length=12, 
        unique=True,
        validators=[RegexValidator(regex=r'^\d{1,2}\.\d{3}\.\d{3}-[0-9Kk]$', message='Inserte un rut válido (ejemplo: xx.xxx.xxx-x)' )]
    )
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField(
        validators=[RegexValidator(regex=r'^\d{9,10}$', message='Ingrese un número de teléfono adecuado (ejemplo: +56912345678)')]
    )
    edad = models.IntegerField(
        validators=[RegexValidator(regex=r'^\d{1,3}$', message='No puede tener una edad con más de 3 dígitos.')]
    )
    correo = models.EmailField(
        validators=[EmailValidator('El correo ingresado no es válido, compruebe el ejemplo: correoejemplo@gmail.com')]
    )
    libros_comprados = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='clientes', null=True, blank=True)
    
