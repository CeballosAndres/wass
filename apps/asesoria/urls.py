from django.urls import path
from .views import *

urlpatterns = [
    path('materia/', seleccionMateria, name='seleccion_materia'),
    path('materia/<str:materia>/tema/', seleccionTema, name='seleccion_tema'),
    path('materia/<str:materia>/tema/<str:tema>/subtema/',
         seleccionSubtema, name='seleccion_subtema'),
    path('materia/<str:materia>/tema/<str:tema>/subtema/<str:subtema>/asesor/',
         seleccionAsesor, name='seleccion_asesor'),
    path('materia/<str:materia>/tema/<str:tema>/subtema/<str:subtema>/asesor/<str:asesor>/hora/<str:hora>',
         nuevaAsesoria, name='nueva_asesoria'),
    path('ver-asesorias/', verAsesorias, name='ver_asesorias'),

]
