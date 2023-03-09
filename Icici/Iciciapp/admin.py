from django.contrib import admin
from .models import Employee_Details

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','designation','doj']
admin.site.register(Employee_Details,EmployeeAdmin)