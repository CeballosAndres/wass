from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path('', views.pAsesorado, name='principal'),
        path('ingreso/', views.ingreso, name='ingreso'),
        path('salir/', views.salir, name='salir'),
        path('registro/', views.registro, name='registro'),
        path('docente/', views.pAsesor, name='docente'),
        path('jfe-dpto/', views.pJefeD, name='jfe-dpto'),
        path('admi/', views.pAdmi, name='admi'),
        path('agendar/', views.agendar, name='agendar'),
        path('ver-asesorias/', views.verAsesorias, name='ver-asesorias'),
        path('config-alumno/', views.cAsesorado, name='config-alumno'),
        path('config-docente/', views.cAsesor, name='config-docente'),
        path('index/', views.index, name='index'),
        path('reportes/', views.reportes, name='reporte'),
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
