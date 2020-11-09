from django.shortcuts import render
from django.http import HttpResponse


def registro(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def mainstudent(request):
    return render(request, 'accounts/main-student.html')
