from rest_framework import serializers
from rest_framework.response import responses
from rest_framework.decorators import api_view
from .models import Employee_Details

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model= Employee_Details
        fields='__all__'