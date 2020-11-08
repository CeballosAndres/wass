from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'accounts/main.html')


def alumno(request):
    return HttpResponse("Hola")
