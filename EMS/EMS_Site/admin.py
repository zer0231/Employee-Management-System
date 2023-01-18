from csv import list_dialects
from django.contrib import admin

from .models import employee_detail, job


# Register your models here.

@admin.register(employee_detail)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email']

@admin.register(job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name']