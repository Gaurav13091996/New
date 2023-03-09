from django.db import models

# Create your models here.
class Employee_Details(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    designation=models.CharField(max_length=20)
    doj=models.DateField()

    class Meta:
        db_table='employee'

