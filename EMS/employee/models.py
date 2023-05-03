from django.db import models

# Create your models here.

class employees(models.Model):
    name= models.CharField(max_length=200)
    contact= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    password= models.CharField(max_length=100)
    department= models.CharField(max_length=200)
    salary= models.CharField(max_length=200)
    date= models.DateField(auto_now=True)