from django_filters import rest_framework as filters

from tasker.models import Tasker

class TaskerFilterSet(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    uf = filters.CharFilter(field_name='user__uf', lookup_expr='iexact')
    city = filters.CharFilter(field_name='user__city', lookup_expr='iexact')

    class Meta:
        model = Tasker
        fields = ['category', 'uf', 'city']
