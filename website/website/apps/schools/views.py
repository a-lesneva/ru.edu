from django.shortcuts import render
from django.http import HttpResponse
from .models import State, Suburb, School
from .filters import SchoolFilter
from django.views.generic import ListView


class SchoolListView(ListView):
    model = School
    template_name = 'schools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        school_filter = SchoolFilter(self.request.GET, queryset = self.get_queryset())
        has_filter = any(field in self.request.GET for field in set(school_filter.get_fields()))
        
        context['filter'] = school_filter
        context['has_filter'] = has_filter
        return context



