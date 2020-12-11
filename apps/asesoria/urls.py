from django.urls import path
from .views import *

urlpatterns = [
    path('nueva/materia/', seleccionMateria, name='seleccion_materia'),
    path('nueva/materia/<str:materia>/tema/', seleccionTema, name='seleccion_tema'),
    path('nueva/materia/<str:materia>/tema/<str:tema>/subtema/',
         seleccionSubtema, name='seleccion_subtema'),
    path('nueva/materia/<str:materia>/tema/<str:tema>/subtema/<str:subtema>/asesor/',
         seleccionAsesor, name='seleccion_asesor'),
]
