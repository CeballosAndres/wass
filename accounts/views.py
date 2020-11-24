from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users

from django.views.generic import DetailView


@unauthenticated_user
def registro(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Add some flash messages before to redirect
            email = form.cleaned_data.get('email')
            messages.success(request, 'Registro exitoso para ' + email)
            return redirect('ingreso')
    context = {'form': form}
    return render(request, 'accounts/registro.html', context)


@unauthenticated_user
def ingreso(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('principal')
        else:
            messages.warning(request, 'Combinación incorrecta de usuario y contraseña.')
    context = {}
    return render(request, 'accounts/ingreso.html', context)


def salir(request):
    logout(request)
    return redirect('ingreso')


@login_required(login_url='ingreso')
@allowed_users(['asesorados', 'asesores', 'jefes'])
def principal(request):
    opciones = []
    group = request.user.groups.all()[0].name
    if group == 'asesorados':
        opciones = {'agendar': 'Agendar',
                    'ver-asesorias': 'Ver Asesorías'}
    elif group == 'asesores':
        opciones = {'agendar': 'Mis asesorías',
                    'ver-asesorias': 'Horario',
                    'index': 'Temario',
                    'reportes': 'Reportes'}
    elif group == 'jefes':
        opciones = {'index': 'Carrera',
                    'reportes': 'Reportes'}
    context = {'opciones': opciones}
    return render(request, 'accounts/principal.html', context)


@login_required(login_url='ingreso')
def pAsesor(request):
    return render(request, 'accounts/ppal-asesor.html')


@login_required(login_url='ingreso')
def pJefeD(request):
    return render(request, 'accounts/ppal-jfedpto.html')


@login_required(login_url='ingreso')
def pAdmi(request):
    return render(request, 'accounts/ppal-adm.html')


@login_required(login_url='ingreso')
def agendar(request):
    return render(request, 'accounts/agendar.html')


@login_required(login_url='ingreso')
def verAsesorias(request):
    return render(request, 'accounts/ver-asesorias.html')


<<<<<<< HEAD
@unauthenticated_user
def cAsesorado(request):
    return render(request, 'accounts/config-asesorado.html')


@unauthenticated_user
def cAsesor(request):
    return render(request, 'accounts/config-asesor.html')
=======
def configurar(request):
    group = request.user.groups.all()[0].name
    user_profile = None
    form = None
    user_email = request.user.email
    # User type
    if group == 'asesorados':
        user_profile = Asesorado.objects.get(usuario=request.user.id)
    else:
        user_profile = Asesor.objects.get(usuario=request.user.id)
    # User data form
    if request.method == 'POST':
        if group == 'asesorados':
            form = AsesoradoForm(request.POST, instance=user_profile)
        else:
            form = AsesorForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos personales actualizados.')
            return redirect('configurar')
    else:
        if group == 'asesorados':
            form = AsesoradoForm(instance=user_profile)
        else:
            form = AsesorForm(instance=user_profile)
    context = {'hide_config': True, 'group': group, 'form': form,
               'user_email': user_email}
    return render(request, 'accounts/configurar.html', context)


@login_required(login_url='ingreso')
def contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # solve autologin!
            messages.success(request, 'Contraseña actualizada')
            return redirect('configurar')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/contrasena.html', context)
>>>>>>> 44c7599605596d130509f4bc6f7c785f86ab813f


@login_required(login_url='ingreso')
def index(request):
    return render(request, 'accounts/index.html')


@login_required(login_url='ingreso')
def reportes(request):
    return render(request, 'accounts/ver-reportes.html')
