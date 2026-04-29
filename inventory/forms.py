from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity_in_stock', 'storage_aisle', 'cost_per_unit']
        # The 'widgets' section adds Bootstrap styling automatically!
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'quantity_in_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'storage_aisle': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
        }