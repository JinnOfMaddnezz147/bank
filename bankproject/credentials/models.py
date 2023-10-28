from django.db import models
from django.contrib.auth.models import User


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Name
    dob = models.DateField()  # DOB
    age = models.IntegerField()  # AGE
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])  # GENDER
    phone_number = models.CharField(max_length=15)  # PHONE NUMBER
    email = models.EmailField()  # MAIL ID
    address = models.TextField()  # ADDRESS
    district = models.ForeignKey(District, on_delete=models.CASCADE)  # District
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Branch
