from django.db import models

class Employee(models.Model):
    employee_firstname= models.CharField(max_length=50)
    employee_lastname = models.CharField(max_length=50)
    employee_salary= models.FloatField()
    employee_age= models.IntegerField()
    employee_phone=models.IntegerField()
    employee_shop=models.ForeignKey(ShoppingCenter,on_delete=models.CASCADE,related_name='employees')


    def __str__(self):
         return f"{self.employee_firstname} {self.employee_lastname}  -- {self.employee_shop}"