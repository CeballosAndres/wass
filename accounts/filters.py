import django_filters
from django.db.models import Q
from django_filters import CharFilter
from .models import Materia


class MateriaFilter(django_filters.FilterSet):
    query = CharFilter(method='my_custom_filter')

    class Meta:
        model = Materia
        fields = ['query']

    def my_custom_filter(self, queryset, name, value):
        return Materia.objects.filter(
            Q(nombre__icontains=value) | Q(clave_materia__icontains=value)
        )
