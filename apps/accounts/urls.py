from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ListarMaterias
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('registro/', views.registro, name='registro'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('salir/', views.salir, name='salir'),
    path('configurar/', views.configurar, name='configurar'),
    path('configurar/contrasena/', views.contrasena, name='contrasena'),
    path('configurar/horario/', views.horario, name='horario'),
    path('configurar/horario/eliminar/<str:pk>/', views.eliminarHorario, name='eliminar_horario'),
    path('index/', views.index, name='index'),
    path('reportes/', views.reportes, name='reportes'),
    path('rep-sem/', views.repSem, name='rep-sem'),
    path('materia/', ListarMaterias.as_view(), name='listar_materias'),
    path('temario/', views.temario, name='temario'),
    path('temario/materia/<str:pk>', views.temarioMateriaEditar, name='temario_materia_editar'),
    path('temario/agregar/', views.temarioAgregarModal, name='temario_agregar_modal'),
    path('temario/agregar/<str:pk>/', views.temarioAgregar, name='temario_agregar'),
    path('temario/eliminar/<str:pk>/', views.temarioEliminar, name='temario_eliminar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
