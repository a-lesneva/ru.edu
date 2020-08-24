from django.contrib import admin
from .models import School, State, Suburb

# Register your models here.
admin.site.register(School)
admin.site.register(Suburb)
admin.site.register(State)