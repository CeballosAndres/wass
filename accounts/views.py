from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def registro(request):
    context = {}
    return render(request, 'accounts/registro.html', context)


def ingreso(request):
    context = {}
    return render(request, 'accounts/ingreso.html', context)


def Pasesorado(request):
    return render(request, 'accounts/ppal-asesorado.html')


def Pasesor(request):
    return render(request, 'accounts/ppal-asesor.html')


def PjefeD(request):
    return render(request, 'accounts/ppal-jfedpto.html')


def Padmi(request):
    return render(request, 'accounts/ppal-adm.html')


def agendar(request):
    return render(request, 'accounts/agendar.html')


def verAsesorias(request):
    return render(request, 'accounts/ver-asesorias.html')


def config(request):
    return render(request, 'accounts/config.html')
