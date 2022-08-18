from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=30)

    def __str__(self):
        return self.id +self.name+self.branch

class Department(models.Model):
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.emp +self.name