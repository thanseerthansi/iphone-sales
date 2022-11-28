from django.contrib import admin
from Sellingapp.models import SellorderModel, SellproductorderModel

# Register your models here.
admin.site.register(SellorderModel)
admin.site.register(SellproductorderModel)