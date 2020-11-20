from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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


def pAsesorado(request):
    return render(request, 'accounts/ppal-asesorado.html')


def pAsesor(request):
    return render(request, 'accounts/ppal-asesor.html')


def pJefeD(request):
    return render(request, 'accounts/ppal-jfedpto.html')


def pAdmi(request):
    return render(request, 'accounts/ppal-adm.html')


def agendar(request):
    return render(request, 'accounts/agendar.html')


def verAsesorias(request):
    return render(request, 'accounts/ver-asesorias.html')


def cAsesorado(request):
    return render(request, 'accounts/config-asesorado.html')


def cAsesor(request):
    return render(request, 'accounts/config-asesor.html')


def index(request):
    return render(request, 'accounts/index.html')


def reportes(request):
    return render(request, 'accounts/ppal-reportes.html')
