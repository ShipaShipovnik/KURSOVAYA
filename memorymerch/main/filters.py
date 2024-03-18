import django_filters
from .models import Tovar


class TovarFilter(django_filters.FilterSet):
    tovarname = django_filters.CharFilter(field_name='tovarname', lookup_expr='icontains')
    tovarprice = django_filters.CharFilter(field_name='tovarprice', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')


    class Meta:
        model = Tovar
        fields = ['tovarname', 'tovarprice','category']