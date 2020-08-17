import django_filters
from django import forms
from .models import School, State

class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label = 'Название школы', lookup_expr='icontains')
    state = django_filters.ModelChoiceFilter(label = 'Штат', queryset=State.objects.all())

    class Meta:
        model = School
        fields = ['name', 'state']