from rest_framework import serializers
from commonapp.serializers import ProductSerializer, StatusSerializer
from .models import *

# class PhoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PhoneModel
#         fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = "__all__"
    def get_status(self,obj):
        if obj.status:
            v_obj = StatusModel.objects.filter(id=obj.status.id)
            v_qs = StatusSerializer(v_obj,many=True)
            return v_qs.data
        else:pass

class OrderdproductSerializer(serializers.ModelSerializer):
    order_id = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    class Meta:
        model = OrderedproductModel
        fields = "__all__"
    def get_order_id(self,obj):
        if obj.order_id:
            v_obj = OrderModel.objects.filter(id=obj.order_id.id)
            v_qs = OrderSerializer(v_obj,many=True)
            return v_qs.data
        else:pass
    def get_product(self,obj):
        if obj.product:
            v_obj = ProductModel.objects.filter(id=obj.product.id)
            v_qs = ProductSerializer(v_obj,many=True)
            return v_qs.data
        else:pass

class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = ReviewModel
        fields = "__all__"
    def get_product(self,obj):
        if obj.product:
            v_obj = ProductModel.objects.filter(obj.product.id)
            v_qs = ProductSerializer(v_obj,many=True)
            return v_qs.data 
         

