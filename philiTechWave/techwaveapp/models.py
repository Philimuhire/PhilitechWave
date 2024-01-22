# techwaveapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class TechSupportService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Default description for the service.")
    
class CybercafeUsage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    usage_date = models.DateField()
    usage_duration_minutes = models.IntegerField()

class TrainingProgram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_days = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




