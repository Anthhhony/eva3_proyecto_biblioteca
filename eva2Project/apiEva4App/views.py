from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AutorSerializer, LibroSerializer, ClienteSerializer
from eva2App.models import Autor, Libro, Cliente
# Create your views here.

# ViewSet para Autor
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# ViewSet para Libro
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# ViewSet para Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer