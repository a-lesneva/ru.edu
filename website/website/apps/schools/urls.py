from django.urls import path
from . import views

app_name = 'schools'
urlpatterns = [
    path('', views.filter_schools, name = 'schools')
   
]