from django import forms
from eva2App.models import Cliente, Autor


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