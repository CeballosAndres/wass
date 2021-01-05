import datetime as dt
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .filters import *
from accounts.models import Asesorado, Asesor, Jefe, Materia, Tema, Subtema, Agenda, TemarioAsesor

from accounts.decorators import allowed_users
from .helpers import enviarEmail


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
        'carrera': carrera
    }
    return render(request, 'asesoria/seleccion_materia.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesorados'])
def seleccionTema(request, materia):
    temas = get_list_or_404(Tema, materia=materia)
    materia_object = get_object_or_404(Materia, id=materia)

    context = {
        'temas': temas,
        'materia': materia_object
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
        'title': 'Selección de Subtema'
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
        'title': 'Selección de Asesor'
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
        # Ajuste para el supuesto de asesorías de la proxima semana
        if faltantes < 0:
            faltantes += 7
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
            asesoria.estado = 'pendiente'
            asesoria.asesorado = asesorado
            asesoria.asesor = asesor
            asesoria.subtema = subtema
            asesoria.save()
            # bloquear el horario del asesor
            agenda.disponible = False
            agenda.save()

            enviarEmail('solicitud', asesoria)
            messages.success(request, 'Solicitud de asesoría enviada.')
            return redirect('accounts:principal')

    context = {
        'title': 'Confirmar asesoría',
        'entrada': 'Describe brevemente la problemática (obligatorio)',
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

    filtro = AsesoriaFilter(request.GET, queryset=asesorias)
    asesorias = filtro.qs

    context = {
        'asesorias': asesorias,
        'filtro': filtro
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
            enviarEmail('aceptación', asesoria)
            messages.success(request, 'Asesoría aceptada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'title': 'Aceptar asesoría',
        'entrada': 'Requisitos previos a la asesoría (opcional)',
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
            enviarEmail('rechazo', asesoria)
            messages.success(request, 'Asesoría rechazada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'title': 'Rechazar asesoría',
        'entrada': 'Razón de rechazo (obligatorio)',
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
            enviarEmail('finalización', asesoria)
            messages.success(request, 'Asesoría finalizada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'title': 'Finalizar asesoría',
        'entrada': 'Comentario final (obligatorio)',
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
            enviarEmail('cancelación', asesoria)
            messages.success(request, 'Asesoría cancelada exitosamente.')
            return redirect('asesoria:ver_asesorias')

    context = {
        'title': 'Cancelar asesoría',
        'entrada': 'Razón de cancelación (obligatorio)',
        'asesoria': asesoria,
        'form': form,
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)


@login_required(login_url='accounts:ingreso')
def detalleAsesoria(request, pk):
    asesoria = get_object_or_404(Asesoria, id=pk)
    context = {
        'title': 'Detalle asesoría',
        'asesoria': asesoria,
    }
    return render(request, 'asesoria/confirmar_asesoria.html', context)


@login_required(login_url='accounts:ingreso')
def reportes(request):
    context = {'title': 'Tipos de reportes'}
    return render(request, 'asesoria/reportes.html', context)


@login_required(login_url='accounts:ingreso')
def repSem(request):
    group = request.user.groups.all()[0].name
    if group == 'asesorados':
        asesorado = Asesorado.objects.get(usuario=request.user.id)
        asesorias = Asesoria.objects.filter(asesorado=asesorado).order_by('fecha_asesoria')
    elif group == 'asesores':
        asesor = Asesor.objects.get(usuario=request.user.id)
        asesorias = Asesoria.objects.filter(asesor=asesor).order_by('fecha_asesoria')
    else:
        # TODO: falta filtrar por jefe
        asesorias = Asesoria.objects.order_by('fecha_asesoria')

    if len(asesorias) == 0:
        messages.warning(request, 'No existen asesorias.')

    context = {
        'title': 'Reporte de asesorías por semestre',
        'asesorias': asesorias,
    }
    return render(request, 'asesoria/rep-sem.html', context)
