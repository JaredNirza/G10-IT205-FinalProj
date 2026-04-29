from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Stationery', 'Stationery'),
        ('Furniture', 'Furniture'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    quantity_in_stock = models.IntegerField()
    storage_aisle = models.CharField(max_length=10)
    cost_per_unit = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.quantity_in_stock} in stock)"