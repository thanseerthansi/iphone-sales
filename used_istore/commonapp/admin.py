from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StatusModel)
# admin.site.register(CityModel)
# admin.site.register(ColorModel)
admin.site.register(ConditionModel)
admin.site.register(ProductModel)
admin.site.register(ImageModel)