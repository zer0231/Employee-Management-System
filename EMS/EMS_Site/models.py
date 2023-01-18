from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.

class employee_detail(models.Model):
    GENDER = [("M","Male"),("F","Female"),("O","others")]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13,blank=True)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    status= models.BooleanField()
    gender = models.CharField(choices=GENDER,max_length=1)
    dob = models.DateField()
    joining_date = models.DateField()
    jobs = models.ManyToManyField("job",blank=True)

class job(models.Model):
    name = models.CharField(max_length=100)
