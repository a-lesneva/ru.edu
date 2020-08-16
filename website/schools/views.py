from django.shortcuts import render
from django.http import HttpResponse
from .models import State, Suburb, School

def is_param_valid(param):
    return param != '' and param is not None

def filterSchools(request):
    qs = School.objects.all()
    states = State.objects.all()
    search_by_name_query = request.GET.get('search_by_name')
    search_by_state_query = request.GET.get('search_by_state')
    active = request.GET.get('search_by_active')

    if is_param_valid(search_by_name_query):
        qs = qs.filter(name__icontains=search_by_name_query)

    if is_param_valid(search_by_state_query) and search_by_state_query != 'Выберите...':
        qs = qs.filter(state__name=search_by_state_query)
        
    if active == 'on':
        qs = qs.filter(active=True) 

    show_all_query = request.GET.get('show_all')
    if show_all_query:
        qs = School.objects.all()
        
    context = {
        'queryset': qs,
        'states': states
    }
    return render(request, 'schools/index.html', context)
