from django.forms import ModelForm
from django import forms
from asesoria.models import Asesoria


class AseroriaSolicitudForm(ModelForm):
    subtema = forms.CharField(widget=forms.TextInput())
    asesor = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Asesoria
        fields = ['fecha_asesoria', 'subtema', 'asesor', 'descripcion', ]
