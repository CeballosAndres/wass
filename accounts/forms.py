from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Asesorado, Asesor, Agenda

from django.utils.dateparse import parse_time
import datetime as dt


HORAS = [(dt.time(hour=h, minute=m), '{:02d}:{:02d}'.format(h, m)) for h in range(7, 19) for m in [0, 30]]
DIAS = [
    ('lunes', 'Lunes'),
    ('martes', 'Martes'),
    ('miercoles', 'Miércoles'),
    ('jueves', 'Jueves'),
    ('viernes', 'Viernes'),
]


class AgendaForm(ModelForm):
    error_messages = {
        'wrong_time': _('La hora de inicio debe ser menor a la de final.'),
    }
    dia_semana = forms.CharField(widget=forms.Select(choices=DIAS))
    hora_inicio = forms.TimeField(widget=forms.Select(choices=HORAS))
    hora_final = forms.TimeField(widget=forms.Select(choices=HORAS))

    class Meta:
        model = Agenda
        fields = ['dia_semana', 'hora_inicio', 'hora_final']

    def clean(self):
        cleaned_data = self.cleaned_data
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_final = self.cleaned_data.get('hora_final')
        if hora_inicio >= hora_final:
            raise ValidationError(
                self.error_messages['wrong_time'],
                code='wrong_time',
            )
        else:
            return cleaned_data


class AsesoradoForm(ModelForm):
    class Meta:
        model = Asesorado
        fields = ['celular', 'nombre', 'carrera']


class AsesorForm(ModelForm):
    class Meta:
        model = Asesor
        fields = ['celular', 'nombre', 'departamento', 'clave_empleado', ]


class CreateUserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'bad_domain': _('El dominio permitido es colima.tecnm.mx .'),
        'user_exists': _('El usuario ya se encuentra registrado.'),
        'user_student_incorrect': _('El correo del alumno esta formado por 8 dígitos mas el dominio.'),
    }

    email = forms.EmailField(
        required=True,
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            user, domain = email.split('@')
            if domain != 'colima.tecnm.mx':
                raise ValidationError(
                    self.error_messages['bad_domain'],
                    code='bad_domain',
                )
            if User.objects.filter(username=email).exists():
                raise ValidationError(
                    self.error_messages['user_exists'],
                    code='user_exists',
                )
            if user.isdigit() and len(user) != 8:
                raise ValidationError(
                    self.error_messages['user_student_incorrect'],
                    code='user_student_incorrect',
                )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
