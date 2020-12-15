from django.forms import ModelForm
from django import forms
from asesoria.models import Asesoria


class AseroriaSolicitudForm(ModelForm):
    subtema_nombre = forms.CharField(widget=forms.TextInput())
    asesor_nombre = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Asesoria
        fields = ['fecha_asesoria', 'asesor_nombre', 'subtema_nombre', 'descripcion', ]
