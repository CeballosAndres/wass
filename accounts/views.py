from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm


def registro(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Add some flash messajes before to redirect
            email = form.cleaned_data.get('email')
            messages.success(request, 'Registro exitoso para ' + email)
        
            return redirect('ingreso')
        
    context = {'form':form}
    return render(request, 'accounts/registro.html', context)


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
def pAsesorado(request):
    return render(request, 'accounts/ppal-asesorado.html')


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


@login_required(login_url='ingreso')
def cAsesorado(request):
    return render(request, 'accounts/config-asesorado.html')


@login_required(login_url='ingreso')
def cAsesor(request):
    return render(request, 'accounts/config-asesor.html')


@login_required(login_url='ingreso')
def index(request):
    return render(request, 'accounts/index.html')


@login_required(login_url='ingreso')
def reportes(request):
    return render(request, 'accounts/ppal-reportes.html')
