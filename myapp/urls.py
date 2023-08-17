from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregar_biblioteca, name='agregar_biblioteca'),
    path('', views.agregar_libro, name='agregar_libro'),
]