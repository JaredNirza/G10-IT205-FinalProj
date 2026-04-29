from django.db import models
from django.contrib.auth.models import User 

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    desk_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"