from datetime import date, datetime, time, timedelta
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .filters import MateriaFilter
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def registro(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Add some flash messages before to redirect
            email = form.cleaned_data.get('email')
            messages.success(request, 'Registro exitoso para ' + email)
            return redirect('accounts:ingreso')
    context = {'hide_navbar': True, 'form': form}
    return render(request, 'accounts/registro.html', context)


@unauthenticated_user
def ingreso(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:principal')
        else:
            messages.warning(request, 'Combinación incorrecta de usuario y contraseña.')
    context = {'hide_navbar': True}
    return render(request, 'accounts/ingreso.html', context)


def salir(request):
    logout(request)
    return redirect('accounts:ingreso')


@login_required(login_url='accounts:ingreso')
def principal(request):
    opciones = []
    group = request.user.groups.all()[0].name
    if group == 'asesorados':
        opciones = {'asesoria:seleccion_materia': 'Agendar',
                    'accounts:ver-asesorias': 'Ver Asesorías'}
        asesorado = Asesorado.objects.get(usuario=request.user.id)
        if not asesorado.carrera:
            messages.warning(request, 'Ingrese sus datos personales.')

    elif group == 'asesores':
        opciones = {'accounts:ver-asesorias': 'Mis asesorías',
                    'accounts:horario': 'Horario',
                    'accounts:temario': 'Temario',
                    'accounts:reportes': 'Reportes'}
        asesor = Asesor.objects.get(usuario=request.user.id)
        materias = TemarioAsesor.objects.filter(asesor=asesor).distinct('materia')
        agendas = Agenda.objects.filter(asesor=asesor).exists()
        if len(materias) == 0:
            messages.warning(request, '<a href="/temario/">Registre materias a asesorar.</a>', extra_tags='safe')
        if not agendas:
            messages.warning(request,
                             '<a href="/configurar/horario/">Registre los horarios en los que asesorará.</a>',
                             extra_tags='safe')

    elif group == 'jefes':
        opciones = {'accounts:index': 'Carrera',
                    'reportes': 'Reportes'}
    context = {'opciones': opciones}
    return render(request, 'accounts/principal.html', context)


@login_required(login_url='accounts:ingreso')
def verAsesorias(request):
    return render(request, 'accounts/ver-asesorias.html')


@login_required(login_url='accounts:ingreso')
def configurar(request):
    group = request.user.groups.all()[0].name
    user_profile = None
    form = None
    user_email = request.user.email
    # User type
    if group == 'asesorados':
        user_profile = Asesorado.objects.get(usuario=request.user.id)
    else:
        user_profile = Asesor.objects.get(usuario=request.user.id)
    # User data form
    if request.method == 'POST':
        if group == 'asesorados':
            form = AsesoradoForm(request.POST, instance=user_profile)
        else:
            form = AsesorForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos personales actualizados.')
            return redirect('accounts:principal')
    else:
        if group == 'asesorados':
            form = AsesoradoForm(instance=user_profile)
        else:
            form = AsesorForm(instance=user_profile)
    context = {'hide_config': True, 'group': group, 'form': form,
               'user_email': user_email}
    return render(request, 'accounts/configurar.html', context)


@login_required(login_url='accounts:ingreso')
def contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # solve autologin!
            messages.success(request, 'Contraseña actualizada')
            return redirect('accounts:configurar')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/contrasena.html', context)


def index(request):
    return render(request, 'accounts/index.html')


@login_required(login_url='accounts:ingreso')
def reportes(request):
    return render(request, 'accounts/reportes.html')


@login_required(login_url='accounts:ingreso')
def repSem(request):
    return render(request, 'accounts/rep-sem.html')


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def horario(request):
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    asesor = Asesor.objects.get(usuario=request.user.id)
    agendas = Agenda.objects.filter(asesor=asesor).order_by('dia', 'hora')

    form = AgendaForm()

    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            dia_semana = form.cleaned_data.get('dia_semana')
            hora_inicio = form.cleaned_data.get('hora_inicio')
            hora_final = form.cleaned_data.get('hora_final')

            while hora_inicio < hora_final:
                Agenda.objects.get_or_create(
                    asesor=asesor,
                    dia=CatalogoDia.objects.get(nombre=dia_semana),
                    hora=CatalogoHora.objects.get(nombre=hora_inicio)
                )
                # Agrega 30 minutos a hora_inicio
                new_date = datetime.combine(date.today(), hora_inicio) + timedelta(minutes=30)
                hora_inicio = new_date.time()

    context = {'agendas': agendas, 'form': form, 'dias': dias}
    return render(request, 'accounts/horario.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def eliminarHorario(request, pk):
    asesor = Asesor.objects.get(usuario=request.user.id)
    agendas = Agenda.objects.filter(asesor=asesor)
    agenda = Agenda.objects.get(id=pk)
    if agenda in agendas:
        agenda.delete()
    return redirect('accounts:horario')


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def temario(request):
    asesor = Asesor.objects.get(usuario=request.user.id)
    materias = TemarioAsesor.objects.filter(asesor=asesor).distinct('materia')

    if len(materias) == 0:
        messages.warning(request, 'No existen materias registradas.')
    filtro = MateriaFilter()

    context = {'materias': materias, 'filtro': filtro}
    return render(request, 'accounts/temario.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def temarioAgregarModal(request):
    asesor = Asesor.objects.get(usuario=request.user.id)
    materias_asesor = TemarioAsesor.objects.filter(asesor=asesor).distinct('materia').values('materia')

    # En caso de tener departamento asignado(asesor) se filtra por este
    if asesor.departamento:
        carreras_departamento = asesor.departamento.carrera_set.all()
        materias = Materia.objects.filter(carrera__in=carreras_departamento)
    else:
        materias = Materia.objects.all()

    # Quitar de las materias a mostrar aquellas que ya fueron agregadas
    materias = materias.exclude(pk__in=materias_asesor)

    filtro = MateriaFilter(request.GET, queryset=materias)
    materias = filtro.qs

    context = {'materias': materias, 'filtro': filtro}
    return render(request, 'accounts/temario_materia.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def temarioAgregar(request, pk):
    asesor = Asesor.objects.get(usuario=request.user.id)
    materia = Materia.objects.get(id=pk)

    temas = materia.tema_set.all()
    for tema in temas:
        subtemas = tema.subtema_set.all()
        for subtema in subtemas:
            TemarioAsesor.objects.get_or_create(asesor=asesor, materia=materia, tema=tema, subtema=subtema)

    messages.success(request, 'Materia agregada')
    return redirect('accounts:temario')


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def temarioEliminar(request, pk):
    materia = Materia.objects.get(id=pk)
    if request.method == 'POST':
        asesor = Asesor.objects.get(usuario=request.user.id)
        TemarioAsesor.objects.filter(asesor=asesor, materia=materia).delete()

        messages.success(request, 'Materia eliminada')
        return redirect('accounts:temario')
    context = {'materia': materia}
    return render(request, 'accounts/temario_eliminar.html', context)


@login_required(login_url='accounts:ingreso')
@allowed_users(['asesores'])
def temarioMateriaEditar(request, pk):
    asesor = Asesor.objects.get(usuario=request.user.id)
    materia = Materia.objects.get(id=pk)

    temas = TemarioAsesor.objects.filter(asesor=asesor, materia=materia).order_by('tema', 'subtema')

    if request.method == 'POST':
        print(request.POST)
        for tema in temas:
            if request.POST.get(str(tema.id)):
                tema.activo = True
            else:
                tema.activo = False
            tema.save()
        messages.success(request, 'Materia actualizada.')
        return redirect('accounts:temario')

    context = {'materia': materia, 'temas': temas}
    return render(request, 'accounts/temario_temas.html', context)


class ListarMaterias(ListView):
    model = Materia


class TemasDeMaterias(DetailView):
    model = Tema
