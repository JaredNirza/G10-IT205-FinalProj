from django.db import models
from staff.models import Employee
from inventory.models import Item

class SupplyRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Fulfilled', 'Fulfilled'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_requested = models.PositiveIntegerField()
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.employee.first_name} requested {self.quantity_requested} {self.item.name}"