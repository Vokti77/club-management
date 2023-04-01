from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='event_cover/')
    detail = models.TextField(max_length=1000)
    place = models.CharField(max_length=1000)
    total = models.IntegerField()
    gained = models.IntegerField(blank=True, default=0)
    deadline = models.DateTimeField(null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)
    READY = {
        ('yes', 'Yes'),
        ('no', 'No',)
    }
    ready_to_distribute = models.CharField(max_length=10, choices=READY, default="no")

    def __str__(self):
        return self.title


class Donate(models.Model):
    doner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.IntegerField()
    PAYMENT = [
        ('bkash', 'Bkash'),
        ('roket', 'Roket'),
        ('nagad', 'Nagad'),
    ]
    method = models.CharField(max_length=50, choices=PAYMENT, default='Bkash')
    mobile_no = models.IntegerField()
    transid = models.CharField(max_length=50)
    date_donated = models.DateField(auto_now_add=True)
    APPROVED = [
        ('no', 'No'),
        ('yes', 'Yes'),
    ]
    isapproved = models.CharField(max_length=25, choices=APPROVED, default='no')


class Person(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class AssetDistribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, default=1)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, default=1)
    amount = models.IntegerField(blank=True, null=True)
    Item = models.TextField(max_length=600, blank=True)
    donate_date = models.DateField(auto_now_add=True)
