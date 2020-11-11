from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path('', views.ingreso),
        path('registro/', views.registro),
        path('alumno/', views.Pasesorado),
        path('docente/', views.Pasesor),
        path('jfe-dpto/', views.PjefeD),
        path('admi/', views.Padmi),
        path('agendar/', views.agendar),
        path('ver-asesorias/', views.verAsesorias),
        path('config/', views.config),
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
