from django.db.models import Q
import django_filters
from pacientes.models import Paciente

class PacienteFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')
    class Meta:
        model = Paciente
        fields = ()
    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(size__icontains=value)
        )
