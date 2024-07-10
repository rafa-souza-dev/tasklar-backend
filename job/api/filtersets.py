import django_filters

from job.models import Job


class JobFilterSet(django_filters.FilterSet):
    uf = django_filters.CharFilter(field_name='tasker__user__uf', lookup_expr='iexact')
    city = django_filters.CharFilter(field_name='tasker__user__city', lookup_expr='iexact')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')

    class Meta:
        model = Job
        fields = ['uf', 'city', 'category']
