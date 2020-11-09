from django.urls import path
from . import views

urlpatterns = [
        path('', views.login),
        path('registro/', views.registro),
        path('alumno/', views.mainstudent),
        ]
