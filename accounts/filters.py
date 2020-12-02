import django_filters
from django_filters import CharFilter
from .models import Materia


class MateriaFilter(django_filters.FilterSet):
    nombre_materia = CharFilter(field_name='nombre', lookup_expr='icontains')
    clave_materia = CharFilter(field_name='clave_materia', lookup_expr='icontains')

    class Meta:
        model = Materia
        fields = ['nombre_materia', 'clave_materia', 'carrera']
