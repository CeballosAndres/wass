from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import Asesorado

@login_required(login_url='ingreso')
def seleccionMateria(request):
    asesorado = Asesorado.objects.get(usuario=request.user.id)
    if not asesorado.carrera:
        messages.info(request, 'Es necesario ingresar la carrera.')
        return redirect('configurar')
    return render(request, 'asesoria/seleccion_materia.html')