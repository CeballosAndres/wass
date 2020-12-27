from django.urls import path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_vies
from .views import ListarMaterias
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.principal, name='principal'),
    path('registro/', views.registro, name='registro'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('salir/', views.salir, name='salir'),
    path('configurar/', views.configurar, name='configurar'),
    path('configurar/contrasena/', views.contrasena, name='contrasena'),
    path('configurar/horario/', views.horario, name='horario'),
    path('configurar/horario/eliminar/<str:pk>/', views.eliminarHorario, name='eliminar_horario'),
    path('contrasena_restablecer/', auth_vies.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done'),
                                                                        extra_context={'hide_logout': True, 'hide_config':True}),
         name='reset_password'),
    path('contrasena_restablecer_enviar/', auth_vies.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('contrasena_restablecer/<uidb64>/<token>/', auth_vies.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('contrasena_restablecer_terminado/', auth_vies.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('materia/', ListarMaterias.as_view(), name='listar_materias'),
    path('temario/', views.temario, name='temario'),
    path('temario/materia/<str:pk>', views.temarioMateriaEditar, name='temario_materia_editar'),
    path('temario/agregar/', views.temarioAgregarModal, name='temario_agregar_modal'),
    path('temario/agregar/<str:pk>/', views.temarioAgregar, name='temario_agregar'),
    path('temario/eliminar/<str:pk>/', views.temarioEliminar, name='temario_eliminar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
