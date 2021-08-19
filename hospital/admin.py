from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'specialist']


admin.site.register(Patient)
admin.site.register(Appointment)
