from django.forms import ModelForm
from django import forms
from accounts.models import Materia


class MateriaForm(ModelForm):
    nombre = forms.CharField(
        widget=forms.Select()
    )

    class Meta:
        model = Materia
        fields = ['nombre']
