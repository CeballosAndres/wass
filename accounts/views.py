from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'accounts/main.html')


def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def alumno(request):
    return HttpResponse("Hola")
