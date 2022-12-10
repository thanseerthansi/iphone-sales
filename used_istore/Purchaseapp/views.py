from django.shortcuts import render
import json
from used_istore.globalimport import *
from used_istore.mypagination import MyLimitOffsetPagination
from commonapp.serializers import ImageSerializer
from .serializers import OrderdproductSerializer, OrderSerializer, ReviewSerializer
from .models import *

# from Purchaseapp.models import PhoneModel



# Create your views here.
# class PhoneView(ListAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # serializer_class =  PhoneSerializer

    # def get_queryset(self):
    #     try:
    #         id = self.request.GET.get('id')
    #         phone = self.request.GET.get('phone_model')
    #         qs = PhoneModel.objects.all()
    #         if id : qs = qs.filter(id=id)
    #         if phone: qs = qs.filter(phone_model = phone)
    #     except:return None
    # def post(self,request):
    #     try:
    #         try:id = self.request.data['id']
    #         except:id=''
            
    #         if id:
    #             phone_qs = PhoneModel.objects.filter(id=id)
    #             if phone_qs.count():
    #                 phone_qs = phone_qs.first()
    #                 phone_obj = PhoneSerializer(phone_qs,data=self.request.data,partial=True)
    #                 msg = "Updatded Successfully"
    #             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
    #         else:
    #             phone_obj = PhoneSerializer(data=self.request.data,partial=True)
    #             msg = "Saved Successfully"
    #         phone_obj.is_valid(raise_exception=True)
    #         phone_obj.save()
    #     except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    # def patch(self,request):
    #     try:
    #         try: id =self.request.data['id']
    #         except:id=''
    #         try: keyword =self.request.data['keyword']
    #         except:keyword=''
    #         try: color =self.request.data['color']
    #         except:color=''
    #         try: phone_model =self.request.data['phone_model']
    #         except:phone_model=''
    #         mandatory = ['keyword','id']
    #         data = Validate(self.request.data,mandatory)
    #         if data==True:
    #             phone_qs = PhoneModel.objects.filter(id=id)
    #             if phone_qs.count():
    #                 phone_qs = phone_qs.first()
    #                 color = json.loads(color)
    #                 phone_model = json.loads(phone_model)
    #                 if keyword=="add":
    #                     if color:
    #                         for i in color:
    #                             color_qs = ColorModel.objects.filter(id=i)
    #                             if color_qs.count():
    #                                 phone_qs.model_color.add(color_qs[0])
    #                                 msg = "Added Successfully"
    #                             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
    #                     if phone_model:
    #                         for p in  PhoneModel:
    #                             Product_qs = ProductModel.objects.filter(id=p)
    #                             if Product_qs.count():
    #                                 phone_qs.phone_model.add(Product_qs[0])
    #                                 msg = "Added Successfully"
    #                             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
    #                 elif keyword=="remove":
    #                     if color:
    #                         for i in color:
    #                             color_qs = ColorModel.objects.filter(id=i)
    #                             if color_qs.count():
    #                                 phone_qs.model_color.remove(color_qs[0])
    #                                 msg = "removed Successfully"
    #                             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
    #                     if phone_model:
    #                         for p in  PhoneModel:
    #                             Product_qs = ProductModel.objects.filter(id=p)
    #                             if Product_qs.count():
    #                                 phone_qs.phone_model.remove(Product_qs[0])
    #                                 msg = "removed Successfully"
    #                             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
    #                 return Response({"Status":status.HTTP_200_OK,"Message":msg})
    #             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
    #     except Exception as e :return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    # def delete(self,request):
    #     try:
    #         id = self.request.data['id']
    #         obj = PhoneModel.objects.filter(id=id)
    #         if obj.count():
    #             obj.delete()
    #             return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
    #         else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
    #     except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class OrderView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OrderSerializer
    pagination_class = MyLimitOffsetPagination
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            orderstatus = self.request.GET.get('status')
            qs = OrderModel.objects.all()
            if id:qs = qs.filter(id=id)
            if orderstatus:qs-qs .filter(status__id=orderstatus)
            return qs.order_by('-id')
        except: return None
    def post(self,request):
        try:
            # print("ok",self.request.data)
            orderdata = self.request.data[0]
            try:id = orderdata['id']
            except:id=''
            try:orderstatus= orderdata['status']
            except:orderstatus=''
            # print("ordrestatus",orderstatus)
            if orderstatus :
                status_qs = StatusModel.objects.filter(status__icontains=orderstatus)
                # print("qs",status_qs)
                if status_qs.count():
                    status_qs = status_qs.first()
            if id:
                order_qs = OrderModel.objects.filter(id=id)
                if order_qs.count():
                    order_qs = order_qs.first()
                    if not status_qs:status_qs = order_qs.status
                    order_obj = OrderSerializer(order_qs,data=orderdata,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No records found with given id"})
            else:
                order_obj= OrderSerializer(data=orderdata,partial=True)
                msg = "Saved Successfully"
            order_obj.is_valid(raise_exception=True)
            order_saveddata = order_obj.save(status = status_qs)
            #product add to ordered table start
            for i in self.request.data:
                # print("i",i)
                try:product = i['product']
                except:product = ''
                if product:
                    product_qs = ProductModel.objects.filter(id=product)
                    if product_qs.count():
                        product_qs = product_qs.first()
                        orderedproduct_qs =  OrderdproductSerializer(data=i,partial = True)
                        orderedproduct_qs.is_valid(raise_exception=True)
                        orderedproduct_qs.save(order_id = order_saveddata,product = product_qs)
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
                # else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Product not found"})
            #product add to ordered table end

            return Response({"Status":status.HTTP_200_OK,"Message":msg,"id":order_saveddata.id,"date":order_saveddata.created_date})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            id=json.loads(id)
            print("id",id)
            if id:
                obj = OrderModel.objects.filter(id__in=id)
                if obj.count():
                    obj.delete()                 
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No id found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class OrderedproductView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OrderdproductSerializer
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            order_id = self.request.GET.get('order_id')
            product  = self.request.GET.get('product')
            qs = OrderedproductModel.objects.all()
            if id:qs = qs.filter(id=id)
            if order_id:qs=qs.filter(order_id__id = order_id)
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
                order_qs = OrderModel.objects.filter(id=order_id)
                if order_qs.count():
                    order_qs = order_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})          
            if product:
                product_qs = ProductModel.objects.filter(id=order_id)
                if product_qs.count():
                    product_qs = product_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            if id:
                orderedproduct_qs = OrderedproductModel.objects.filter(id=id)
                if orderedproduct_qs.count():
                    orderedproduct_qs = orderedproduct_qs.first()
                    if not product: product_qs = orderedproduct_qs.product
                    if not order_id: order_qs = orderedproduct_qs.order_id
                    orderedproduct_obj = OrderdproductSerializer(orderedproduct_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"  
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"}) 
            else:
                orderedproduct_obj = OrderdproductSerializer(data=self.request.data,partial=True)
                msg = "Saved Successfully"
            orderedproduct_obj.is_valid(raise_exception=True)
            orderedproduct_obj.save(order_id = order_qs,product = product_qs)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})      
        except Exception as e : return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            id=json.loads(id)
            if id:
                obj = OrderedproductModel.objects.filter(id__in=id)
                if obj.count():
                    obj.delete()                 
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No id found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class ReviewView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer
    pagination_class = MyLimitOffsetPagination
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            product = self.request.GET.get('product')
            # print("product",product)
            review_star = self.request.GET.get('review_star')
            qs = ReviewModel.objects.all()
            if id: qs = qs.filter(id=id)
            # print("okk")
            if product: qs = qs.filter(product__id=product)
            # print("okkllmsidg",qs)
            if review_star : qs = qs.filter(review_star=review_star)
            return qs.order_by('-id')
        except:return None
    def post(self,request):
        try:
            # imagelist = []
            # print("data",self.request.data)
            # try: images = self.request.FILES.getlist('images')
            # except:images=''
            # print("image",images)
            # try: images = self.request.FILES.getlist('images')
            # except:images=''
            # if images:
            #     for image in images:
            #         print("image",image)
            #         image_obj = ImageSerializer(data={'image':image},partial=True)
            #         image_obj.is_valid(raise_exception=True)
            #         image_saved = image_obj.save()
            #         imagelist.append(image_saved.id)
            try:id = self.request.data['id']
            except : id = ''
            try: product = self.request.data['product']
            except:product = ''
            if product:
                product_qs = ProductModel.objects.filter(id=product)
                if product_qs.count(): product_qs = product_qs.first()
            if id :  
                review_qs = ReviewModel.objects.filter(id=id)
                if review_qs.count():
                    review_qs = review_qs.first()
                    if not product: product_qs =  review_qs.product
                    review_obj = ReviewSerializer(review_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
            else:
                review_obj = ReviewSerializer(data=self.request.data,partial=True)
                # print("revieobj",review_obj)
                msg = "Saved Sucessfully"
                
            review_obj.is_valid(raise_exception=True)
            review_data = review_obj.save(product= product_qs)
            try: images = self.request.FILES.getlist('imagelist')
            except:images=''
            if images:
                for image in images:
                    # print("image",image)
                    image_obj = ImageSerializer(data={'image':image},partial=True)
                    image_obj.is_valid(raise_exception=True)
                    image_saved = image_obj.save()
                    review_data.images.add(image_saved)    
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id= self.request.data['id']
            id = json.loads(id)
            if id:
                obj = ReviewModel.objects.filter(id__in=id)
                if obj.count():
                    obj.delete()                 
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No id found"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})