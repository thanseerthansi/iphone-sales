from django.db import models
from commonapp.models import ProductModel, StatusModel

# Create your models here.
class SellorderModel(models.Model):
    customer_name = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    contact = models.CharField(max_length=100,blank=True)
    status = models.ForeignKey(StatusModel,on_delete = models.DO_NOTHING)
    city = models.CharField(max_length=100,blank=True)
    total_price  = models.FloatField(default=0.0)
    description  = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class SellproductorderModel(models.Model):
    sellorder_id = models.ForeignKey(SellorderModel,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.DO_NOTHING)
    price = models.FloatField(default=0.0)
    condition = models.CharField(max_length=100,blank=True)
    storage = models.CharField(max_length=100,blank=True)
    color  = models.CharField(max_length=100,blank=True)
    quantity  = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
