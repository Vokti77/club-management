from django.db import models
from django.contrib.auth.models import User


class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/')
    BLOOD = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A-', 'A-'),
        ('B-', 'B-')
    ]
    blood = models.CharField(max_length=5, choices=BLOOD, default='B+', null=True)


    def __str__(self):
        return self.user.username


class MemberProfile(models.Model):
    STATUS = [
        ('1', 'Approved'),
        ('2', 'Pending')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    batch = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/')
    cv = models.FileField(upload_to='cv/')
    status = models.CharField(max_length=2, choices=STATUS, default='2', null=True)

    def __str__(self):
        return self.user.username
