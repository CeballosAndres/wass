from django.urls import path
from .views import *

urlpatterns = [
    path('', verAsesorias, name='ver_asesorias'),
    path('materia/', seleccionMateria, name='seleccion_materia'),
    path('materia/<str:materia>/tema/', seleccionTema, name='seleccion_tema'),
    path('materia/<str:materia>/tema/<str:tema>/subtema/',
         seleccionSubtema, name='seleccion_subtema'),
    path('materia/<str:materia>/tema/<str:tema>/subtema/<str:subtema>/asesor/',
         seleccionAsesor, name='seleccion_asesor'),
    path('materia/<str:materia>/tema/<str:tema>/subtema/<str:subtema>/asesor/<str:asesor>/hora/<str:hora>',
         nuevaAsesoria, name='nueva_asesoria'),
    path('reportes/', reportes, name='reportes'),
    path('rep-sem/', repSem, name='rep-sem'),
    path('<str:pk>/', detalleAsesoria, name='detalle_asesoria'),
    path('<str:pk>/aceptar/', aceptarAsesoria, name='aceptar_asesoria'),
    path('<str:pk>/cancelar/', cancelarAsesoria, name='cancelar_asesoria'),
    path('<str:pk>/rechazar/', rechazarAsesoria, name='rechazar_asesoria'),
    path('<str:pk>/finalizar/', finalizarAsesoria, name='finalizar_asesoria'),
]
