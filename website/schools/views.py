from django.shortcuts import render
from django.http import HttpResponse
from .models import State, Suburb, School
from .filters import SchoolFilter

def filter_schools(request):
    schools_list = School.objects.all()
    school_filter = SchoolFilter(request.GET, queryset = schools_list)
    has_filter = any(field in request.GET for field in set(school_filter.get_fields()))
    
    return render(request, 'schools/index.html', {
        'filter': school_filter,
        'has_filter': has_filter
        })


