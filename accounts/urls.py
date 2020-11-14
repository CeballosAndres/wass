from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path('', views.index),
        path('registro/', views.registro),
        path('alumno/', views.pAsesorado),
        path('docente/', views.pAsesor),
        path('jfe-dpto/', views.pJefeD),
        path('admi/', views.pAdmi),
        path('agendar/', views.agendar),
        path('ver-asesorias/', views.verAsesorias),
        path('config-alumno/', views.cAsesorado),
        path('config-docente/', views.cAsesor),
        path('ingreso/', views.ingreso),
        path('reportes/', views.reportes)
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
