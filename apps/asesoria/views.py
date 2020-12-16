import datetime as dt
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from accounts.models import Asesorado, Asesor, Materia, Tema, Subtema, Agenda, TemarioAsesor

from accounts.decorators import allowed_users


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesorados'])
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
        'titulo': 'Agendar asesoría'
    }
    return render(request, 'asesoria/seleccion_materia.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesorados'])
def seleccionTema(request, materia):
    temas = get_list_or_404(Tema, materia=materia)
    materia_object = get_object_or_404(Materia, id=materia)

    context = {
        'temas': temas,
        'materia': materia_object,
        'titulo': 'Selección de Tema'
    }
    return render(request, 'asesoria/seleccion_tema.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesorados'])
def seleccionSubtema(request, materia, tema):
    subtemas = get_list_or_404(Subtema, tema=tema)
    materia_object = get_object_or_404(Materia, id=materia)
    tema_object = get_object_or_404(Tema, id=tema)

    context = {
        'subtemas': subtemas,
        'materia': materia_object,
        'tema': tema_object,
        'titulo': 'Selección de Subtema'
    }
    return render(request, 'asesoria/seleccion_subtema.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesorados'])
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
        'titulo': 'Selección de Asesor'
    }
    return render(request, 'asesoria/seleccion_asesor.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesorados'])
def nuevaAsesoria(request, materia, tema, subtema, asesor, hora):
    asesor = get_object_or_404(Asesor, id=asesor)
    subtema = get_object_or_404(Subtema, id=subtema)
    materia = get_object_or_404(Materia, id=materia)
    agenda = get_object_or_404(Agenda, id=hora)
    # agregar diferencia de dias
    hoy = dt.date.today().weekday()
    if hoy <= 4:
        faltantes = int(agenda.dia.nombre) - hoy
    else:
        faltantes = 7 - hoy + int(agenda.dia.nombre)
    dia = dt.date.today() + dt.timedelta(days=faltantes)
    fecha_asesoria = dt.datetime.combine(dia, agenda.hora.nombre)

    form = SolicitudAseroriaForm()

    if request.method == 'POST':
        print('post')
        form = SolicitudAseroriaForm(request.POST)
        if form.is_valid():
            asesoria = form.save(commit=False)
            asesorado = get_object_or_404(Asesorado, usuario=request.user.id)
            asesoria.fecha_asesoria = fecha_asesoria
            # almacena el id de la agenda para faciliar consutlas TODO: mejorar
            asesoria.agenda = hora
            asesoria.asesorado = asesorado
            asesoria.asesor = asesor
            asesoria.subtema = subtema
            asesoria.save()
            # bloquear el horario del asesor
            agenda.disponible = False
            agenda.save()
            messages.success(request, 'Solicitud de asesoría enviada.')
            return redirect('accounts:principal')

    context = {
        'titulo': 'Confirmar asesoría',
        'entrada': 'Describe brevemente la problemática',
        'form': form,
        'asesoria': {
            'asesor': asesor,
            'materia': materia,
            'subtema': subtema,
            'fecha_asesoria': fecha_asesoria,
        }
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)


@login_required(login_url='accounts:ingreso')
def verAsesorias(request):
    group = request.user.groups.all()[0].name
    if group == 'asesorados':
        asesorado = get_object_or_404(Asesorado, usuario=request.user.id)
        asesorias = Asesoria.objects.filter(asesorado=asesorado)
    else:
        asesor = get_object_or_404(Asesor, usuario=request.user.id)
        asesorias = Asesoria.objects.filter(asesor=asesor)

    if len(asesorias) == 0:
        messages.warning(request, 'No existen asesorías agendadas.')

    context = {
        'asesorias': asesorias,
        'titulo': 'Mis asesorías'
    }
    return render(request, 'asesoria/ver_asesorias.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def aceptarAsesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, id=pk)

    form = AceptarAsesoriaForm(instance=asesoria)

    if request.method == 'POST':
        form = AceptarAsesoriaForm(request.POST, instance=asesoria)
        if form.is_valid():
            asesoria = form.save(commit=False)
            asesoria.estado = 'aceptada'
            asesoria.save()
            messages.success(request, 'Asesoría aceptada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'titulo': 'Aceptar asesoría',
        'entrada': 'Requisitos previos a la asesoría',
        'asesoria': asesoria,
        'form': form,
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def rechazarAsesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, id=pk)
    form = RechazarAsesoriaForm(instance=asesoria)

    if request.method == 'POST':
        form = RechazarAsesoriaForm(request.POST, instance=asesoria)
        if form.is_valid():
            asesoria = form.save(commit=False)
            asesoria.estado = 'rechazada'
            asesoria.save()
            agenda = get_object_or_404(Agenda, id=asesoria.agenda)
            agenda.disponible = True
            agenda.save()
            messages.success(request, 'Asesoría rechazada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'titulo': 'Rechazar asesoría',
        'entrada': 'Razón de rechazo',
        'asesoria': asesoria,
        'form': form,
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def finalizarAsesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, id=pk)
    form = FinalizarAsesoriaForm(instance=asesoria)

    if request.method == 'POST':
        form = FinalizarAsesoriaForm(request.POST, instance=asesoria)
        if form.is_valid():
            asesoria = form.save(commit=False)
            asesoria.estado = 'finalizada'
            asesoria.save()
            messages.success(request, 'Asesoría finalizada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'titulo': 'Finalizar asesoría',
        'entrada': 'Comentario final',
        'asesoria': asesoria,
        'form': form,
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores', 'asesorados'])
def cancelarAsesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, id=pk)
    form = CancelacionAsesoriaForm(instance=asesoria)

    if request.method == 'POST':
        form = CancelacionAsesoriaForm(request.POST, instance=asesoria)
        if form.is_valid():
            asesoria = form.save(commit=False)
            asesoria.estado = 'cancelada'
            asesoria.save()
            agenda = get_object_or_404(Agenda, id=asesoria.agenda)
            agenda.disponible = True
            agenda.save()
            messages.success(request, 'Asesoría cancelada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'titulo': 'Cancelar asesoría',
        'entrada': 'Razón de cancelación',
        'asesoria': asesoria,
        'form': form,
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)



@login_required(login_url='accounts:ingreso')
def detalleAsesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, id=pk)

    context = {
        'titulo': 'Detalle asesoría',
        'asesoria': asesoria,
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)