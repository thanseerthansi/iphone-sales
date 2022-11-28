from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usermodel(AbstractUser):
    conact = models.CharField(max_length=100,blank=True)
    is_status = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)