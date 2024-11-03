from django.contrib import admin
from eva2App.models import Libro, Autor, Cliente


# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'genero', 'editorial', 'precio', 'n_paginas', 'stock')
    search_fields = ('titulo', 'autor')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo')
    search_fields = ('nombre','apellido')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'telefono', 'edad', 'correo', 'libros_comprados')
    search_fields = ('rut', 'nombre')