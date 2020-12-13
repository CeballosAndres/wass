from django.db import models
from django.contrib.auth.models import User
import datetime as dt

HORAS = [(dt.time(hour=h, minute=m), '{:02d}:{:02d}'.format(h, m)) for h in range(7, 20) for m in [0, 30]]
DIAS = [
    ('0', 'Lunes'),
    ('1', 'Martes'),
    ('2', 'Miércoles'),
    ('3', 'Jueves'),
    ('4', 'Viernes'),
]


class Jefe(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    celular = models.CharField(max_length=200, blank=True, null=True)
    clave_empleado = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Jefe'
        verbose_name_plural = 'Jefes'

    def __str__(self):
        return self.usuario.username


class Departamento(models.Model):
    nombre = models.CharField(max_length=255)
    jefe = models.ForeignKey(Jefe, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento,
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    competencia = models.TextField(null=True, blank=True)
    clave_materia = models.CharField(max_length=20, null=True, blank=True, unique=True)
    carrera = models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return self.nombre


class Asesorado(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    carrera = models.ForeignKey(Carrera, null=True, on_delete=models.SET_NULL, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Asesorado'
        verbose_name_plural = 'Asesorados'

    def __str__(self):
        return self.usuario.username


class CatalogoDia(models.Model):
    nombre = models.CharField(null=False, blank=False, max_length=10, choices=DIAS, unique=True)

    class Meta:
        verbose_name = 'Catalogo día'
        verbose_name_plural = 'Catalogo días'

    def __str__(self):
        return self.nombre


class CatalogoHora(models.Model):
    nombre = models.TimeField(null=False, blank=False, max_length=10, choices=HORAS, unique=True)

    class Meta:
        verbose_name = 'Catalogo hora'
        verbose_name_plural = 'Catalogo horas'

    def __str__(self):
        return str(self.nombre)


class Tema(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=300, null=False, blank=False)
    competencia = models.TextField(null=False, blank=True)
    materia = models.ForeignKey(Materia, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.nombre


class Subtema(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=300, null=False, blank=False)
    tema = models.ForeignKey(Tema, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Subtema'
        verbose_name_plural = 'Subtemas'

    def __str__(self):
        return self.nombre


class Asesor(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    clave_empleado = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, blank=True)
    subtetmas = models.ManyToManyField(Subtema, through='TemarioAsesor')
    horarios = models.ManyToManyField(CatalogoDia, through='Agenda')

    class Meta:
        verbose_name = 'Asesor'
        verbose_name_plural = 'Asesores'

    def __str__(self):
        return self.usuario.username


class Agenda(models.Model):
    asesor = models.ForeignKey(Asesor, null=False, on_delete=models.CASCADE)
    dia = models.ForeignKey(CatalogoDia, null=True, on_delete=models.SET_NULL, choices=DIAS)
    hora = models.ForeignKey(CatalogoHora, null=True, on_delete=models.SET_NULL, choices=HORAS)
    disponible = models.BooleanField('Disponible/no disponible', default=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        unique_together = (('asesor', 'dia', 'hora'),)


class TemarioAsesor(models.Model):
    materia = models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, null=False, blank=False, on_delete=models.CASCADE)
    subtema = models.ForeignKey(Subtema, null=False, blank=False, on_delete=models.CASCADE)
    asesor = models.ForeignKey(Asesor, null=False, blank=False, on_delete=models.CASCADE)
    activo = models.BooleanField('Activo/no activo', default=False)

    class Meta:
        verbose_name = 'Temario del asesor'
        verbose_name_plural = 'Temarios del asesor'
        unique_together = (('materia', 'tema', 'subtema', 'asesor'),)

    def __str__(self):
        return self.materia.nombre
