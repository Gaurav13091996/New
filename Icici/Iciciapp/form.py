from .models import Employee_Details
from django import forms
from django.core import validators
from django.forms import widgets

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model=Employee_Details
        fields=['id','name','age','designation','doj']
