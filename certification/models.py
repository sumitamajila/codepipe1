from django.db import models

# Create your models here.
"""
certification details
first_name - text
last_name - text
gender - radio button
email - email
name - text
date - date
cost - float
marks - integer
validity - integer with drop down list
center_address - text area
result - boolean 
status - we will create it later

"""


class CertificationDetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=255)
    date = models.DateField()
    cost = models.FloatField()
    marks = models.IntegerField()
    validity = models.IntegerField()
    center_address = models.TextField(max_length=500)
    result = models.BooleanField()
    status = models.BooleanField(default=True)
    feedback = models.TextField(max_length=500, default="Good")
    ratings = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - ({self.name}) "


class Employee(models.Model):
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     email = models.EmailField(max_length=30)
     salary = models.FloatField()

     def __str__(self):
        return f"({self.first_name} {self.last_name})"






