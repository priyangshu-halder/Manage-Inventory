from django.db import models

# Create your models here.
class Inventory_model(models.Model):
    unique_id=models.AutoField(primary_key=True, unique=True)
    name=models.CharField(max_length=200)
    quantity=models.IntegerField(default=None)
    price=models.IntegerField(default=None)
    status=models.CharField(max_length=20)
    date=models.CharField(max_length=12)
