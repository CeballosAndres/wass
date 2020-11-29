from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Departamento)
admin.site.register(Carrera)
admin.site.register(Materia)
admin.site.register(Jefe)
admin.site.register(Asesor)
admin.site.register(Asesorado)
admin.site.register(DiaAtencion)
admin.site.register(HorarioAtencion)
admin.site.register(Agenda)
