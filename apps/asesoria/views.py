from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.models import Asesorado, Asesor, Materia, Tema, Subtema, Agenda, TemarioAsesor


@login_required(login_url='accounts:ingreso')
def seleccionMateria(request):
    asesorado = get_object_or_404(Asesorado, usuario=request.user.id)
    if not asesorado.carrera:
        messages.info(request, 'Es necesario ingresar la carrera.')
        return redirect('accounts:configurar')

    carrera = asesorado.carrera
    materias = get_list_or_404(Materia, carrera=carrera)
    context = {
        'materias': materias,
        'carrera': carrera,
    }
    return render(request, 'asesoria/seleccion_materia.html', context)


@login_required(login_url='accounts:ingreso')
def seleccionTema(request, materia):
    temas = get_list_or_404(Tema, materia=materia)
    materia_object = get_object_or_404(Materia, id=materia)

    context = {
        'temas': temas,
        'materia': materia_object,
    }
    return render(request, 'asesoria/seleccion_tema.html', context)


@login_required(login_url='accounts:ingreso')
def seleccionSubtema(request, materia, tema):
    subtemas = get_list_or_404(Subtema, tema=tema)
    materia_object = get_object_or_404(Materia, id=materia)
    tema_object = get_object_or_404(Tema, id=tema)

    context = {
        'subtemas': subtemas,
        'materia': materia_object,
        'tema': tema_object,
    }
    return render(request, 'asesoria/seleccion_subtema.html', context)


@login_required(login_url='accounts:ingreso')
def seleccionAsesor(request, materia, tema, subtema):
    asesores = TemarioAsesor.objects.filter(subtema=subtema, activo=True)
    agendas = Agenda.objects.filter(asesor__in=asesores.values('asesor'), disponible=True)

    if len(asesores) == 0 and len(agendas) == 0:
        messages.warning(request, 'No existen asesores o disponibilidad de horario.')

    context = {
        'asesores': asesores,
        'agendas': agendas,
        'materia': materia,
        'tema': tema,
        'subtema': subtema,

    }
    return render(request, 'asesoria/seleccion_asesor.html', context)


@login_required(login_url='accounts:ingreso')
def nuevaAsesoria(request, materia, tema, subtema, asesor, hora):
    materia = get_object_or_404(Materia, id=materia)

    context = {
        'materia': materia,
    }
    return render(request, 'asesoria/nueva_asesoria.html', context)
