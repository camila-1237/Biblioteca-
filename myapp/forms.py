from django import forms
from .models import Biblioteca, Libro

class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['name', 'direction']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['name', 'ISBN', 'autor', 'estado']
