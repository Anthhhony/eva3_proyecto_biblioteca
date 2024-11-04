from django.shortcuts import render, redirect
from . import forms
from eva2App.models import Cliente, Autor, Libro
from eva2App.forms import ClienteForm, AutorForm, LibroForm

def menu(request):
    return render(request, "templatesApp/menu.html")

def registro(request):
    registro = Cliente.objects.all()
    data = {"registro":registro}
    return render(request, "templatesApp/index.html", data)

def agregar_cliente(request):
    form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
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

def eliminar_cliente(request, id):
    dato = Cliente.objects.get(id = id)
    dato.delete()
    return redirect(registro)

def actualizar_cliente(request, id):
    project = Cliente.objects.get(id = id)
    form = ClienteForm(instance=project)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return registro(request)
    data = {"form":form}
    return render(request, "templatesApp/agregar.html", data)

def mostrar_autor(request):
    autores = Autor.objects.all()
    return render(request, 'templatesApp/autores.html', {'autores':autores})

def agregar_autor(request):
    titulo = 'Agregar'
    form = AutorForm()
    if request.method == 'POST':
        form= AutorForm(request.POST)
        if form.is_valid():
            db = Autor(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                correo= form.cleaned_data['correo']
            )
            db.save()
        return redirect(mostrar_autor)
    return render(request, 'templatesApp/form_autor.html', {
        'form':form,
        'titulo':titulo
    })

def actualizar_autor(request,id):
    titulo = 'Editar'
    autor = Autor.objects.get(id = id)
    form = AutorForm(instance=autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
        return redirect(mostrar_autor)
    return render(request, 'templatesApp/form_autor.html', {
        'form':form,
        'titulo':titulo
    })

def eliminar_autor(request, id):
    autor = Autor.objects.get(id = id)
    autor.delete()
    return redirect(mostrar_autor)

def mostrar_libros(request):
    libro = Libro.objects.all()
    return render(request, 'templatesApp/vistaLibros.html', {'libro':libro})

def agregar_libro(request):
    titulo = 'Agregar'
    form = LibroForm()
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            db = Libro(
                codigo = form.cleaned_data['codigo'],
                titulo = form.cleaned_data['titulo'],
                genero = form.cleaned_data['genero'],
                editorial = form.cleaned_data['editorial'],
                precio = form.cleaned_data['precio'],
                n_paginas = form.cleaned_data['n_paginas'],
                stock = form.cleaned_data['stock'],
                autor = form.cleaned_data['autor']
            )
            db.save()
        return redirect(mostrar_libros)
    return render(request, 'templatesApp/registroLibro.html', {
        'form':form,
        'titulo':titulo
    })

def actualizar_libro(request, id):
    titulo = 'Editar'
    libro = Libro.objects.get(id=id)
    form = LibroForm(instance=libro)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        return redirect(mostrar_libros)
    return render(request, 'templatesApp/registroLibro.html', {
        'form':form,
        'titulo':titulo
    })
    
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect(mostrar_libros)


# Create your views here.
