from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path('', views.principal, name='principal'),
        path('registro/', views.registro, name='registro'),
        path('ingreso/', views.ingreso, name='ingreso'),
        path('salir/', views.salir, name='salir'),
        path('configurar/', views.configurar, name='configurar'),
        path('configurar/contrasena/', views.contrasena, name='contrasena'),
        path('configurar/horario/', views.horario, name='horario'),
        path('configurar/horario/eliminar/<str:pk>/', views.eliminarHorario, name='eliminar_horario'),
        path('configurar/temas/', views.temas, name='temas'),
        path('agendar/', views.agendar, name='agendar'),
        path('ver-asesorias/', views.verAsesorias, name='ver-asesorias'),
        path('index/', views.index, name='index'),
        path('reportes/', views.reportes, name='reportes'),
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
