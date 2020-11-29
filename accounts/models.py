from django.db import models
from django.contrib.auth.models import User


class Jefe(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    celular = models.CharField(max_length=200, null=True)
    clave_empleado = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.usuario


class Departamento(models.Model):
    nombre = models.CharField(max_length=255)
    jefe = models.ForeignKey(Jefe, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento,
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    competencia = models.TextField()
    clave_materia = models.CharField(max_length=20)

    def __str__():
        return self.nombre


class Asesorado(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    carrera = models.ForeignKey(Carrera, null=True, on_delete=models.SET_NULL, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.usuario.username


class DiaAtencion(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Asesor(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    clave_empleado = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, blank=True)

    horarios = models.ManyToManyField(DiaAtencion, through='Agenda')

    def __str__(self):
        return self.usuario.username


class HorarioAtencion(models.Model):
    inicio = models.TimeField()

    def __str__(self):
        return str(self.inicio)


class Agenda(models.Model):
    asesor = models.ForeignKey(Asesor, null=False, on_delete=models.CASCADE)
    dia = models.ForeignKey(DiaAtencion, null=True, on_delete=models.SET_NULL)
    hora = models.ForeignKey(HorarioAtencion, null=True, on_delete=models.SET_NULL)

