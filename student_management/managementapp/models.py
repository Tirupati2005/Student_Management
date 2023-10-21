from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    percentage=models.FloatField()
    course=models.CharField(max_length=200)
    contact=models.IntegerField(null=True)
    email=models.CharField(max_length=200,null=True)
    college=models.CharField(max_length=200,null=True)
    degree=models.CharField(max_length=200,null=True)
    year=models.IntegerField(null=True)
