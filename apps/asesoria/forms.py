from django.forms import ModelForm
from django import forms
from asesoria.models import Asesoria


class SolicitudAseroriaForm(ModelForm):
    class Meta:
        model = Asesoria
        fields = ['descripcion']


class DetalleAseroriaForm(ModelForm):
    class Meta:
        model = Asesoria
        fields = ['descripcion', 'requisitos', 'razon_cancelada', 'razon_rechazada', 'comentario_finalizada']


class CancelacionAsesoriaForm(ModelForm):

    class Meta:
        model = Asesoria
        fields = ['razon_cancelada']


class AceptarAsesoriaForm(ModelForm):
    class Meta:
        model = Asesoria
        fields = ['requisitos']


class FinalizarAsesoriaForm(ModelForm):
    class Meta:
        model = Asesoria
        fields = ['comentario_finalizada']


class RechazarAsesoriaForm(ModelForm):
    class Meta:
        model = Asesoria
        fields = ['razon_rechazada']