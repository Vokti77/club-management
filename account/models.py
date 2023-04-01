from django.db import models
from django.contrib.auth.models import User


class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='image/')

    def __str__(self):
        return self.user.username


class EmployeeProfile(models.Model):
    STATUS = [
        ('1', 'Approved'),
        ('2', 'Pending')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='image/')
    cv = models.FileField(upload_to='cv/')
    status = models.CharField(max_length=2, choices=STATUS, default='2', null=True)

    def __str__(self):
        return self.user.username
