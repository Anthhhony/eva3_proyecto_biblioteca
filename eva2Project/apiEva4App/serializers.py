from rest_framework import serializers
from eva2App.models import Autor, Libro, Cliente  # Importa los modelos de la app antigua

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='autor-detail')

    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'apellido', 'correo', 'url']

class LibroSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='libro-detail')
    class Meta:
        model = Libro
        fields = '__all__'
        
    def to_representation(self, instance):
    # Llamamos a la representación original
        representation = super().to_representation(instance)

    # Extraemos el campo 'url' y lo removemos de la representación
        url = representation.pop('url', None)
    
    # Agregamos el campo 'url' al final de la representación
        if url:
            representation['url'] = url
    
        return representation

class ClienteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cliente-detail')
    class Meta:
        model = Cliente
        fields = '__all__'
    def to_representation(self, instance):
        # Llamamos a la representación original
            representation = super().to_representation(instance)
        
        # Extraemos el campo 'url' y lo removemos de la representación
            url = representation.pop('url', None)
        
        # Agregamos el campo 'url' al final de la representación
            if url:
                representation['url'] = url
        
            return representation
