from django.urls import path
from .views import *

urlpatterns = [
    path('', seleccionMateria, name='seleccion_materia'),
]
