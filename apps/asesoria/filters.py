import django_filters
from .models import Asesoria


class AsesoriaFilter(django_filters.FilterSet):
    class Meta:
        model = Asesoria
        fields = ['estado']
