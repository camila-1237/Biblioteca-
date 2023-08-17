from django.shortcuts import render, redirect
from .models import Biblioteca, Libro
from .forms import BibliotecaForm, LibroForm

def agregar_biblioteca(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista')
    else:
        form = BibliotecaForm()
    
    return render(request, 'agregar_biblioteca.html', {'form': form})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista')
    else:
        form = LibroForm()
    
    return render(request, 'agregar_libro.html', {'form': form})