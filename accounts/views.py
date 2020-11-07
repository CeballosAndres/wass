from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'accounts/dashboard.html')


def alumno(request):
    return HttpResponse("Hola")
