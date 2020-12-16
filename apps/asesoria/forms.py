from django.forms import ModelForm
from django import forms
from asesoria.models import Asesoria


class SolicitudAseroriaForm(ModelForm):
    class Meta:
        model = Asesoria
        fields = ['descripcion']


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
