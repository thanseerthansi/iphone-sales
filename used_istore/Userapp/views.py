from django.shortcuts import render
from used_istore.globalimport import *
from Userapp.serializers import UserSerializer
from Userapp.models import Usermodel
from django.contrib.auth.hashers import make_password
# Create your views here.
class Userview(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            userid = self.request.user.id
            qs = Usermodel.objects.all()
            user = self.request.GET.get('user')
            admin = self.request.GET.get("admin")
            if user: qs = qs.filter(id=userid)
            if admin: qs=qs.filter(is_admin=True)
            return qs
        except: return None
    def post(self,request):
        userobj = ""
        try:id=self.request.data['id']
        except:id=''
        try:username = self.request.data['username']
        except:username=''
        try:password = self.request.data['password']
        except:password = ''
         
        try:
            mandatory = ['username','password']
            data = Validate(self.request.data,mandatory)
            if id:
                try:
                    # print("datapost",self.request.data)
                    user = Usermodel.objects.filter(id=id)
                    if user.count():
                        user = user.first()
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"User not found"})
                    # if email != user.email:comm
                    #     email_listqs = list(UserModel.objects.all().values_list('email',flat=True)) 
                    #     if email in email_listqs:return Response({"Status":status.HTTP_208_ALREADY_REPORTED,"Message":"Email Already Exist"})
                    serializer = UserSerializer(user,data=request.data,partial= True)
                    serializer.is_valid(raise_exception=True)
                    if password:
                        msg = "user details and password updated successfully"
                        user_obj = serializer.save(password = make_password(password))
                    else: 
                        msg = "User details updated successfully"
                        user_obj = serializer.save()
                    
                    return Response({"Status":status.HTTP_200_OK,"Message":msg})
                except Exception as e:
                    if  user_obj : user_obj.delete()
                    else : pass
                    return  Response({
                        "Status":status.HTTP_400_BAD_REQUEST,
                        "Message":f"Excepction occured {e}"
                    })
            else:
                if data == True:                
                    try:
                        serializer = UserSerializer(data=request.data, partial=True)
                        serializer.is_valid(raise_exception=True)
                        msg = "Created New User"
                        user_obj = serializer.save(password=make_password(self.request.data['password']))    
                        return Response({"Status":status.HTTP_200_OK,"Message":msg})
                    except Exception as e :
                        return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
                else : return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":data})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        try:
            id= self.request.data['id']
            if id:
                obj = Usermodel.objects.filter(id=id)
                if obj.count():
                    obj.delete()
                    return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record found with given id"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Id not found"})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})