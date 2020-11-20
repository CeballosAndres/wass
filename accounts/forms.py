from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'bad_domain': _('El dominio permitido es @colima.tecnm.mx .'),
        'user_exists': _('El usuario ya se encuentra registrado.'),
    }
    email = forms.EmailField(required=True, label=_("Email"), max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}))

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
            if User.objects.filter(username=user).exists():
                raise ValidationError(
                    self.error_messages['user_exists'],
                    code='user_exists',
                )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"].split('@')[0]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user