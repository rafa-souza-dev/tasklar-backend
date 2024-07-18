import django_filters
from service.models import Service

class ServiceFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date', lookup_expr='iexact')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')

    class Meta:
        model = Service
        fields = ['date', 'status']
