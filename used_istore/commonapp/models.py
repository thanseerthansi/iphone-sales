from django.db import models


# Create your models here.

class StatusModel(models.Model):
    status = models.CharField(max_length=100,blank=True)
    code = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

# class CityModel(models.Model):
#     city = models.CharField(max_length=100,blank=True)
#     description = models.TextField(blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)

# class ColorModel(models.Model):
#     color = models.CharField(max_length=100,blank=True)
#     description = models.TextField(blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
class CategoryModel(models.Model):
    category = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class ModelnameModel(models.Model):
    model_name = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class ConditionModel(models.Model):
    condition = models.CharField(max_length=100,blank=True)
    description  = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class ImageModel(models.Model):
    image = models.ImageField(upload_to='Image',blank=True,null=True)
    # color = models.ForeignKey(ColorModel,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class ProductModel(models.Model):
    title = models.CharField(max_length=100,blank=True)
    # condition = models.ForeignKey(ConditionModel,on_delete=models.CASCADE)
    # storage = models.CharField(max_length=100,blank=True)
    category = models.CharField(max_length=100,blank=True)
    model_name = models.CharField(max_length=100,blank=True)
    colors = models.CharField(max_length=100,blank=True)
    oldfromprice = models.FloatField(default=0.0)
    sellfromprice = models.FloatField(default=0.0)
    sellprice = models.CharField(max_length=200,blank=True)#storage-condition-price,.....
    buyprice = models.CharField(max_length=200,blank=True)
    sellstatus = models.BooleanField(default=True)
    buystatus = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    images = models.ManyToManyField(ImageModel)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class TestimonialModel(models.Model):
    name = models.CharField(max_length=100,blank=True)
    place = models.CharField(max_length=100,blank=True)
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    