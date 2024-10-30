from django.shortcuts import render, redirect
from . import forms
from eva2App.models import Cliente
from eva2App.forms import formularioChetado

def registro(request):
    registro = Cliente.objects.all()
    data = {"registro":registro}
    return render(request, "templatesApp/index.html", data)

def agregar(request):
    form = forms.formulario()
    if request.method == "POST":
        form = forms.formulario(request.POST)
        if form.is_valid():
            db = Cliente(
                rut = form.cleaned_data['rut'],
                nombre = form.cleaned_data['nombre'],
                telefono = form.cleaned_data['telefono'],
                edad = form.cleaned_data['edad'],
                correo = form.cleaned_data['correo']
            )
            db.save()
    data = {"form":form}
    return render(request, "templatesApp/agregar.html", data)

def eliminar(request, id):
    dato = Cliente.objects.get(id = id)
    dato.delete()
    return redirect("../")

def actualizar(request, id):
    project = Cliente.objects.get(id = id)
    form = formularioChetado(instance=project)
    if request.method == "POST":
        form = formularioChetado(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return registro(request)
    data = {"form":form}
    return render(request, "templatesApp/agregar.html", data)

# Create your views here.
