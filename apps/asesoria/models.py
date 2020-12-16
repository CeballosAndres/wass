from django.db import models
from accounts.models import Asesorado, Asesor, Subtema

ESTADOS_ASESORIA = [
    ('pendiente', 'Pendiente'),
    ('aceptada', 'Aceptada'),
    ('rechazada', 'Rechazada'),
    ('cancelada', 'Cancelada'),
    ('finalizada', 'Finalizada'),
]


class Asesoria(models.Model):
    fecha_solicitud = models.DateTimeField(auto_now_add=True, null=False)
    fecha_asesoria = models.DateTimeField('Fecha asesoría', null=False)
    estado = models.CharField('Estado actual', max_length=45, choices=ESTADOS_ASESORIA, default='pendiente')
    descripcion = models.TextField('Descripción', null=True, blank=True)
    requisitos = models.TextField('Requisitos previos a la asesoría', null=True, blank=True)
    comentario_finalizada = models.TextField('Comentarios: asesoría finalizada', null=True, blank=True)
    razon_cancelada = models.TextField('Razón de cancelación', null=True, blank=True)
    razon_rechazada = models.TextField('Razón de rechazo', null=True, blank=True)
    asesorado = models.ForeignKey(Asesorado, null=False, on_delete=models.PROTECT)
    asesor = models.ForeignKey(Asesor, null=False, on_delete=models.PROTECT)
    subtema = models.ForeignKey(Subtema, null=False, on_delete=models.PROTECT)
    agenda = models.IntegerField()

    class Meta:
        verbose_name = 'Asesoria'
        verbose_name_plural = 'Asesorias'

    def __str__(self):
        return str(self.id)
