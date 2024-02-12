from django.db import models

# Create your models here.
class School(models.Model):
    School_Name=models.CharField(max_length=100)
    Principal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
