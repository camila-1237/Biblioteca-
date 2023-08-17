from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    name = models.CharField(max_length=50, help_text='ingrese el nombre de la biblioteca')
    direction = models.CharField(max_length=100, help_text='ingrese la direccion')

class Libro(models.Model):
    name = models.CharField(max_length=50, help_text='ingrese el nombre el libro')
    ISBN = models.CharField(max_length=13, help_text='ingrese el ISBN del libro')
    autor = models.CharField(max_length=50, help_text='Ingrese el autor del libro')
    estado = models.CharField(max_length=8, help_text='ingrese el estado del libro')