from django.db import models
from django.contrib.auth.models import User
from internshop.product.models import Product

# Create your models here.
#ีuser = User.objects.create_user('john', 'lennon@thebeatles.com', '12345678')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
#>>> user.last_name = 'Lennon'
#>>> user.save()

class OrderItem(models.Model):
    
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField()
    

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField()
    
