# from django.shortcuts import render
from used_istore.globalimport import *
from commonapp.serializers import (ConditionSerializer, ImageSerializer, ProductSerializer,
    StatusSerializer)
from commonapp.models import ConditionModel, ImageModel, ProductModel, StatusModel
import json
from used_istore.mypagination import MyLimitOffsetPagination
# from Purchaseapp.models import PhoneModel
# from Purchaseapp.serializers import PhoneSerializer
# Create your views here.
class StatusView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = StatusSerializer
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            qs = StatusModel.objects.all()
            if id: qs = qs.filter(id=id)
            return qs
        except :return None
  
    def post(self,request):
        try:
            print("data",self.request.data)
            try: id = self.request.data['id']
            except:id=''
            if id:
                status_qs = StatusModel.objects.filter(id=id)
                if status_qs.count():
                    status_qs = status_qs.first()
                    status_obj = StatusSerializer(status_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"  
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"}) 
            else:
                status_obj = StatusSerializer(data=self.request.data,partial=True)
                msg = "Saved Successfully"
              
            status_obj.is_valid(raise_exception=True)
           
            status_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e : return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            id = self.request.data['id']
            if id : 
                obj = StatusModel.objects.filter(id=id)
                if obj.count():
                    obj.delete()
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"id not found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

# class CityView(ListAPIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = CitySerializer
#     def get_queryset(self):
#         try:
#             id = self.request.GET.get('id')
#             qs = CityModel.objects.all()
#             if id: qs = qs.filter(id=id)
#         except :return None
    
#     def post(self,request):
#         try:
#             try: id = self.request.data['id']
#             except:id=''
#             if id:
#                 city_qs = CityModel.objects.filter(id=id)
#                 if city_qs.count():
#                     city_qs = city_qs.first()
#                     city_obj = CitySerializer(city_qs,data=self.request.data,partial=True)
#                     msg = "Updated Successfully"  
#                 else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"}) 
#             else:
#                 city_obj = CitySerializer(data=self.request.data,partial=True)
#                 msg = "Saved Successfully"
#             city_obj.is_valid(raise_exception=True)
#             city_obj.save()
#             return Response({"Status":status.HTTP_200_OK,"Message":msg})
#         except Exception as e : return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
#     def delete(self,request):
#         try:
#             id = self.request.data['id']
#             if id : 
#                 obj = CityModel.objects.filter(id=id)
#                 if obj.count():
#                     obj.delete()
#                     return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
#                 else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
#             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"id not found"})
#         except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

# class ColorView(ListAPIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = ColorSerializer
#     def get_queryset(self):
#         try:
#             id = self.request.GET.get('id')
#             qs = ColorModel.objects.all()
#             if id: qs = qs.filter(id=id)
#         except :return None
     
#     def post(self,request):
#         try:
#             try: id = self.request.data['id']
#             except:id=''
#             if id:
#                 color_qs = ColorModel.objects.filter(id=id)
#                 if color_qs.count():
#                     color_qs = color_qs.first()
#                     color_obj = ColorSerializer(color_qs,data=self.request.data,partial=True)
#                     msg = "Updated Successfully"  
#                 else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"}) 
#             else:
#                 color_obj = ColorSerializer(data=self.request.data,partial=True)
#                 msg = "Saved Successfully"
#             color_obj.is_valid(raise_exception=True)
#             color_obj.save()
#             return Response({"Status":status.HTTP_200_OK,"Message":msg})
#         except Exception as e : return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
   
#     def delete(self,request):
#         try:
#             id = self.request.data['id']
#             if id : 
#                 obj = ColorModel.objects.filter(id=id)
#                 if obj.count():
#                     obj.delete()
#                     return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
#                 else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
#             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"id not found"})
#         except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class ImageView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ImageSerializer
    def get_queryset(self):
        try:
            id = self.request.data['id']
            qs = ImageModel.objects.all()
            if id: qs = qs.filter(id=id)
            return qs
        except : return None
    def post(self,request):
        try:
            for i in self.request.data:
                try: id = i['id']
                except:id=''
                if id:
                    image_qs = ImageModel.objects.filter(id=id)
                    if image_qs.count():
                        image_qs = image_qs.first()
                        image_obj = ImageSerializer(image_qs,data=i,partial=True)
                        msg = "Updated Successfully"
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
                else:
                    image_obj = ImageSerializer(data=i,partial=True)
                    msg = "Saved successfully"
                image_obj.is_valid(raise_exception=True)
                image_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = ImageModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
class ConditionView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ConditionSerializer
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            qs = ConditionModel.objects.all()
            if id: qs = qs.filter(id=id)
            return qs
        except :return None
        
    def post(self,request):
        try:
            try: id = self.request.data['id']
            except:id=''
            if id:
                condition_qs = ConditionModel.objects.filter(id=id)
                if condition_qs.count():
                    condition_qs = condition_qs.first()
                    condition_obj = ConditionSerializer(condition_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"  
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"}) 
            else:
                condition_obj = ConditionSerializer(data=self.request.data,partial=True)
                msg = "Saved Successfully"
            condition_obj.is_valid(raise_exception=True)
            condition_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e : return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

    def delete(self,request):
        try:
            print("self.request.data['id']",self.request.data['id'])
            id = self.request.data['id']
            id=json.loads(id)
            
            if id:
                obj = ConditionModel.objects.filter(id__in=id)
                print("okk")
                if obj.count():
                    print("okk")
                    obj.delete() 
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No id found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class ProductView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    pagination_class = MyLimitOffsetPagination
    def get_queryset(self):
        try:
            # print("dddddd",self.request.GET.get('model_name'))
            id = self.request.GET.get('id')
            buystatus = self.request.GET.get('buystatus')
            sellstatus = self.request.GET.get('sellstatus')
            phone = self.request.GET.get('model_name')
            qs = ProductModel.objects.all()
            if id : qs = qs.filter(id=id)
            if phone : qs =  qs.filter(model_name__icontains = phone)
            if buystatus: qs = qs.filter(buystatus = True)
            if sellstatus: qs = qs.filter(sellstatus=True)
            return qs
        except: return None
    def post(self,request):
        try:
            # print("data",self.request.data)
            #creat field in Phonemodel
            # try: 
                
            #     if self.request.data[0]['id']:
            #         phone_obj = PhoneSerializer(data=self.request.data[0],partial=True)
            #         phone_obj.is_valid(raise_exception=True)
            #         phone_obj_data = phone_obj.save()
            #         # to  add color to phone model table model color
            #         try:color =self.request.data[0]['color']
            #         except:color = ''
            #         if color:
            #             for c in color:
            #                 color_qs = ColorModel.objects.filter(id=c)
            #                 if color_qs.count():
            #                     phone_obj_data.model_color.add(color_qs[0])
            #         #colo add end 
            # except Exception as e :return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
            # for i in self.request.data:
            try:id=self.request.data['id']
            except: id = ''
            # try: condition = i['condition']
            # except : condition =''
            # if condition :
            #     condition_qs = ConditionModel.objects.filter(id=condition)
            #     if condition_qs.count():
            #         condition_obj = condition_qs.first()
            if id:
                product_qs = ProductModel.objects.filter(id=id)
                if product_qs.count():
                    product_qs = product_qs.first()
                    # if not condition:condition_obj = product_qs.condition
                    product_obj = ProductSerializer(product_qs,data=self.request.data,partial=True)
                    msg = "Updated successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given data"})
            else:
                product_obj  =  ProductSerializer(data=self.request.data,partial=True)
                msg = "Saved Successfully"
            product_obj.is_valid(raise_exception=True)
            # print("save")
            product_obj_data=product_obj.save()
            #to addd color and phone_model in phone table ...
            # phone_obj_data.phone_model.add(product_obj_data)    
            # to add images 
            # print("imageto")
            try: images = self.request.FILES.getlist('images')
            except:images=''
            if images:
                for image in images:
                    print("image",image)
                    image_obj = ImageSerializer(data={'image':image},partial=True)
                    image_obj.is_valid(raise_exception=True)
                    image_saved = image_obj.save()
                    product_obj_data.images.add(image_saved)           
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def patch(self,request):
        try:
            try:id = self.request.data['id']
            except:id=''
            try:keyword = self.request.data['keyword']
            except:keyword = ''
            mandatory = ['keyword','id']
            data = Validate(self.request.data,mandatory)
            if data==True:
                product_qs = ProductModel.objects.filter(id=id)
                if product_qs.count():
                    product_qs = product_qs.first()
                    image = json.loads(self.request.data['images'])
                    for i in image:
                        if keyword == "add":
                            image_qs = ImageModel.objects.filter(id=i)
                            if image_qs.count():
                                product_qs.images.add(i)
                                msg = "image added successfully"                            
                            else :return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":i+"Not found"})
                        elif keyword =="remove" :
                            product_list =list( product_qs.images.all().values_list('id',flat=True))
                            if i in product_list:
                                product_qs.images.remove(i)
                                msg = "image removed successfully"
                                productwithimage = ProductModel.objects.filter(images=int(i)) 
                                if productwithimage.count():
                                    pass
                                   
                                else:
                                    img=ImageModel.objects.filter(id=i)
                                    if img.count():
                                        img.delete()
                                        
                            return Response({"Status":status.HTTP_200_OK,"Message":msg})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":data})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            id=json.loads(id)
            if id:
                obj = ProductModel.objects.filter(id__in=id)
                if obj.count():
                    # modelname= obj[0].model_name
                    obj.delete()
                    # productlist = list(ProductModel.objects.filter(model_name__icontains = modelname).values_list('id',flat=True))
                    # if productlist.count():
                        # pass
                    # else:
                    #     phone_qs = PhoneModel.objects.filter(model_name = modelname)
                    #     if phone_qs.count():
                    #         phone_qs.delete()
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No id found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})