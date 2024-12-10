from rest_framework import serializers
from eva2App.models import Autor, Libro, Cliente  # Importa los modelos de la app antigua

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='autor-detail')
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='libro-detail')
    class Meta:
        model = Libro
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cliente-detail')
    class Meta:
        model = Cliente
        fields = '__all__'
