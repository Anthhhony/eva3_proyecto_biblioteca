from django import forms
from eva2App.models import Cliente, Autor, Libro


class FormularioCliente(forms.Form):
    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    edad = forms.IntegerField()
    correo = forms.EmailField()

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"
        
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.attrs = {
                'class':'form-container'
            }        