from django.shortcuts import render
from django.http import HttpResponse


def registro(request):
    return render(request, 'accounts/registro.html')


def ingreso(request):
    return render(request, 'accounts/ingreso.html')


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
