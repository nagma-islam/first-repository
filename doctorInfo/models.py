from django.db import models

# Create your models here.
class Doctor(models.Model):
    dname=models.CharField(max_length=30)
    dspecialist=models.CharField(max_length=30)
    dcontact=models.IntegerField()
    dage=models.IntegerField()

