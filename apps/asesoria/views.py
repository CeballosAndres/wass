from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import Asesorado, Materia


@login_required(login_url='accounts:ingreso')
def seleccionMateria(request):
    asesorado = Asesorado.objects.get(usuario=request.user.id)
    if not asesorado.carrera:
        messages.info(request, 'Es necesario ingresar la carrera.')
        return redirect('accounts:configurar')

    materias = Materia.objects.filter(carrera=asesorado.carrera)
    
    context = {
        'materias': materias,
    }
    return render(request, 'asesoria/seleccion_materia.html', context)

