import django_filters
from django_filters import ModelChoiceFilter
from django.forms import TextInput
from .models import Tovar,Categories



class TovarFilter(django_filters.FilterSet):
    tovarname = django_filters.CharFilter(field_name='tovarname', lookup_expr='icontains')
    category = ModelChoiceFilter(queryset=Categories.objects.all())
    

    class Meta:
        model = Tovar
        fields = ['tovarname','category__catgname']