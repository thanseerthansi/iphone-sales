from django.db import models
from commonapp.models import ImageModel, ProductModel, StatusModel


# Create your models here.

# class PhoneModel(models.Model):
#     name = models.CharField(max_length=100,blank=True)
#     # model_color = 
#     phone_model = models.ManyToManyField(ProductModel)
#     images = models.ManyToManyField(ImageModel)
#     description = models.TextField(blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
 
class OrderModel(models.Model):
    customer_name = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    contact = models.CharField(max_length=100,blank=True)
    email  = models.CharField(max_length=100,blank=True)
    status = models.ForeignKey(StatusModel,on_delete = models.DO_NOTHING)
    city = models.CharField(max_length=100,blank=True)
    subtotal_price = models.FloatField(default=0.0)
    total_price  = models.FloatField(default=0.0)
    delivery_charge = models.FloatField(default=0.0)
    vat = models.FloatField(default=0.0)
    description  = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class OrderedproductModel(models.Model):
    order_id = models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.DO_NOTHING)
    price = models.FloatField(default=0.0)
    condition = models.CharField(max_length=100,blank=True)
    storage = models.CharField(max_length=100,blank=True)
    color  = models.CharField(max_length=100,blank=True)
    quantity  = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class ReviewModel(models.Model):
    customer = models.CharField(max_length=100,blank=True)
    product  = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    email = models.CharField(max_length=100,blank=True)
    images = models.ManyToManyField(ImageModel)
    review_star = models.IntegerField(default=0)
    status = models.BooleanField(default=True) 
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
