from django.shortcuts import render

import json
from used_istore.globalimport import *
from Sellingapp.models import SellorderModel, SellproductorderModel
from Sellingapp.serializers import SellorderSerializer, SellproductorderSerializer
from commonapp.models import ProductModel, StatusModel
from used_istore.mypagination import MyLimitOffsetPagination

# Create your views here.
class SellorderView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SellorderSerializer
    pagination_class = MyLimitOffsetPagination
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            sellorderstatus = self.request.GET.get('status')
            qs = SellorderModel.objects.all()
            if id:qs = qs.filter(id=id)
            if sellorderstatus:qs=qs .filter(status__id=sellorderstatus)
            return qs
        except: return None
    def post(self,request):
        try:
            print("data",self.request.data)
            sellorderdata = self.request.data[0]
            try:id = sellorderdata['id']
            except:id=''
            try:sellorderstatus= sellorderdata['status']
            except:sellorderstatus=''
            if sellorderstatus :
                status_qs = StatusModel.objects.filter(status__icontains=sellorderstatus)
                if status_qs.count():
                    status_qs = status_qs.first()
            if id:
                sellorder_qs = SellorderModel.objects.filter(id=id)
                if sellorder_qs.count():
                    sellorder_qs = sellorder_qs.first()
                    sellorder_obj = SellorderSerializer(sellorder_qs,data=sellorderdata,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No records found with given id"})
            else:
                sellorder_obj= SellorderSerializer(data=sellorderdata,partial=True)
                msg = "Saved Successfully"
            sellorder_obj.is_valid(raise_exception=True)
            sellorder_saveddata = sellorder_obj.save(status = status_qs)
            #product add to sellordered table start
            for i in self.request.data:
                try:product = i['product']
                except:product = ''
                if product:
                    product_qs = ProductModel.objects.filter(id=product)
                    if product_qs.count():
                        product_qs = product_qs.first()
                        sellproductorder_qs =  SellproductorderSerializer(data=i,partial = True)
                        sellproductorder_qs.is_valid(raise_exception=True)
                        sellproductorder_qs.save(sellorder_id = sellorder_saveddata,product = product_qs)
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
                # else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Product not found"})
            #product add to sellordered table end

            return Response({"Status":status.HTTP_200_OK,"Message":msg,"id":sellorder_saveddata.id,"date":sellorder_saveddata.created_date})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            id=json.loads(id)
            if id:
                obj = SellorderModel.objects.filter(id__in=id)
                if obj.count():
                    obj.delete()                 
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No id found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class SellproductorderView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SellproductorderSerializer
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            order_id = self.request.GET.get('order_id')
            print("orderid",order_id)
            product  = self.request.GET.get('product')
            qs =SellproductorderModel.objects.all()
            if id:qs = qs.filter(id=id)
            if order_id:qs=qs.filter(sellorder_id__id = order_id)
            if product:qs =qs.filter(product__id = product)
            return qs.order_by('-id')
        except: return None
    def post(self,request):
        try:
            try: id = self.request.data['id']
            except:id=''
            try: order_id = self.request.data['order_id']
            except:order_id=''
            try: product = self.request.data['product']
            except:product=''
            if order_id:
                sellorder_qs = SellorderModel.objects.filter(id=order_id)
                if sellorder_qs.count():
                    sellorder_qs = sellorder_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})          
            if product:
                product_qs = ProductModel.objects.filter(id=order_id)
                if product_qs.count():
                    product_qs = product_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            if id:
                sellorderedproduct_qs = SellproductorderModel.objects.filter(id=id)
                if sellorderedproduct_qs.count():
                    sellorderedproduct_qs = sellorderedproduct_qs.first()
                    if not product: product_qs = sellorderedproduct_qs.product
                    if not order_id: order_qs = sellorderedproduct_qs.order_id
                    sellorderedproduct_obj = SellproductorderSerializer(sellorderedproduct_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"  
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"}) 
            else:
                sellorderedproduct_obj = SellproductorderSerializer(data=self.request.data,partial=True)
                msg = "Saved Successfully"
            sellorderedproduct_obj.is_valid(raise_exception=True)
            sellorderedproduct_obj.save(order_id = order_qs,product = product_qs)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})      
        except Exception as e : return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            id=json.loads(id)
            if id:
                obj = SellproductorderModel.objects.filter(id__in=id)
                if obj.count():
                    obj.delete()                 
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No id found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
