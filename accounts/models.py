from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=255)


class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    competencia = models.TextField()
    clave_materia = models.CharField(max_length=20)
