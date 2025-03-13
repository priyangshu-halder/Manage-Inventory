from .models import Inventory_model
from django.forms import ModelForm

class Listing_form(ModelForm):
    class Meta:
        model=Inventory_model
        fields=[
            'name',
            'quantity',
            'price',
            'status',
            'date',
        ]