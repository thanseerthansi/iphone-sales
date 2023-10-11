from django.db import models

# Create your models here.
class BannerModel(models.Model):
    banner_name = models.CharField(max_length=100,blank=True)
    banner_image = models.ImageField(upload_to='Image',blank=True,null=True)
    banner_heading = models.CharField(max_length=100,blank=True)
    banner_redirect = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class ContactModel(models.Model):
    contact = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)