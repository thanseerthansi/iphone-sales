from rest_framework import serializers
from .models import *

# class OrderfullSerializer(serializers.ModelSerializer):
#     status = serializers.SerializerMethodField()
#     class Meta:
#         model = OrderModel
#         fields = ['status','created_date','total_price']
#     def get_status(self,obj):
#         if obj.status:
#             v_obj = StatusModel.objects.filter(id=obj.status.id)
#             v_qs = StatusSerializer(v_obj,many=True)
#             return v_qs.data
#         else:pass
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields ='__all__'