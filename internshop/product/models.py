from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField()
    
