from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product,through="CartItem")


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    products=models.ForeignKey(Product,on_delete=models.PROTECT)


class Order(models.Model):
    order_id=models.CharField(primary_key=True,max_length=50)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address_line_1=models.CharField(null=False,max_length=100)
    address_line_2=models.CharField(null=False,max_length=100)
    city=models.CharField(null=False,max_length=100)
    state=models.CharField(null=False,max_length=100)
    pincode=models.IntegerField(null=False)
    phone_no=models.BigIntegerField(null=False)
    