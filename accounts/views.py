from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def registro(request):
    context = {}
    return render(request, 'accounts/registro.html', context)


def ingreso(request):
    context = {}
    return render(request, 'accounts/ingreso.html', context)


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
    return render(request, 'accounts/ver-reportes.html')
