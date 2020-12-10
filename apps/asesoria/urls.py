from django.urls import path
from .views import *

urlpatterns = [
    path('nueva/', seleccionMateria, name='seleccion_materia'),
]
