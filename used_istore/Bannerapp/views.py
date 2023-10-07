from used_istore.globalimport import *
from .serializers import BannerSerializer, ContactSerializer
from .models import BannerModel, ContactModel

# Create your views here.
class BannerView(ListAPIView):
    serializer_class = BannerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        try:
            qs = BannerModel.objects.all()
            id = self.request.GET.get('id')
            name = self.request.GET.get('banner_name') 
            if id: qs = qs.filter(id=id)
            if name : qs = qs.filter(banner_name=name)
            return qs
        except:return None
    def post(self,request):
        try:
            try: id = self.request.data['id']
            except:id = ""
            if id: 
                banner_qs = BannerModel.objects.filter(id=id)
                if banner_qs.count():
                    banner_qs = banner_qs.first()
                    banner_obj= BannerSerializer(banner_qs,data=self.request.data,partial=True)
                    msg = "Updated successfully"
                else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Data not found with given id"})
            else:
                banner_obj = BannerSerializer(data=self.request.data,partial=True)
                msg = "Saved successfully"
            
            banner_obj.is_valid(raise_exception=True)
            banner_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})    
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            if id : 
                obj = BannerModel.objects.filter(id=id)
                if obj.count():
                    obj.delete()
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"id not found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

            
    
class ContactView(ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        try:
            qs = ContactModel.objects.all()
            # print("qqqqqqqqqsssssssssssss",qs)
            id = self.request.GET.get('id')
            if id: qs = qs.filter(id=id)
            return qs
        except:return None
    def post(self,request):
        try:
            try: id = self.request.data['id']
            except:id = ""
            if id: 
                contact_qs = ContactModel.objects.filter(id=id)
                if contact_qs.count():
                    contact_qs = contact_qs.first()
                    contact_obj= ContactSerializer(contact_qs,data=self.request.data,partial=True)
                    msg = "Updated successfully"
                else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Data not found with given id"})
            else:
                contact_obj = ContactSerializer(data=self.request.data,partial=True)
                msg = "Saved successfully"
            
            contact_obj.is_valid(raise_exception=True)
            contact_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})    
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id = self.request.data['id']
            if id : 
                obj = ContactModel.objects.filter(id=id)
                if obj.count():
                    obj.delete()
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted Successfully"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"id not found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

            
    