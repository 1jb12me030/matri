from django.core.checks.messages import Error
from django.shortcuts import render
from rest_framework.views import APIView
from .serialise import PackageSerialiser, PaymentDetailsSerialiser, UserRegisterSerialiser,LoginSerializer
from rest_framework.response import Response
from app.models import *
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Register(APIView):
    # authentication_classes=[SessionAuthentication,BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            pk=request.GET.get('pk')
            chek=UserRegister.objects.filter(mobile_number=pk)
            if(chek):
                serialise=UserRegisterSerialiser(chek,many=True)
                return Response({"status":200,'details':serialise.data})
            else:
                return Response({"status":403,"message":"Mobile number not found"})
        except Exception as e:
            print(e)
            return Response({"status":404,"message":"Something wrong"})



    def post(self,request):
        try:
            data=request.data
            chek=UserRegister.objects.filter(mobile_number=data['mobile_number']).first()
            if(chek):
                return Response({'message':"Mobile number already exist"})
            serialize1=UserRegisterSerialiser(data=data)
            if(serialize1.is_valid()):
                serialize1.save()
                return Response({'status':200,'payload':serialize1.data,'message':"Data added successfull"})
            else:
                return Response({'status':403,'errors':serialize1.errors,'message':"Invalid Data"})
        except Exception as e:
            print(e)
            return Response({
                'status':404,
                'message':'Something went wrong',
                'data':{}
                })
            
            
            
    #Update data here
    def patch(self,request):
        try:
            data=request.GET.get('pk')
        # req=request.data
            chek=UserRegister.objects.filter(mobile_number=data)
            if not chek:
                 return Response({"s tatus":403,'message':"Mobile number not found"})
            serialise=UserRegisterSerialiser(chek,data=request.data,partial=True)
            print(serialise)
            if(serialise.is_valid()):
                serialise.save()
                return Response({'status':201,'message':"Data has been updated successfully"})
            else:
                return Response({'status':404,'error':serialise.data,'message':"Data Invalid"})
        except Exception as e:
            print(e)
            return Response({'status':404,'message':"Something went wrong"})

    #Delete from table here
    def delete(self,request):
        try:
            pk=request.GET.get('pk')
            mobile=UserRegister.objects.filter(mobile_number=pk)
            if(mobile):
                mobile.delete()
                return Response({'status':201,'message':'Data has been deteted'})
            else:
                return Response({'status':403,'message':'Mobile number not found'})
        except Exception as e:
            return Response({'status':404,'message':'something went wrong'})

class Login(APIView):
    """
    Log in a matrimony
    """
    def post(self,request):
        try:
            data=request.data
            serialiser=LoginSerializer(data = data)
            if serialiser.is_valid():
                mobile_number=serialiser.data['mobile_number']
                password=serialiser.data['password']
                if not User.objects.filter(username = mobile_number).exists():
                    return Response(
                        {
                            'status':False,
                            'message':'user not found',
                            'data':{}
                        }
                    )
                user_obj = authenticate(username=mobile_number,password=password)

                if user_obj is None:
                    return Response({
                        'status':False,
                        'message':'Invalid password',
                        'data':{}
                    })
                token=Token.objects.get_or_create(user = user_obj)
                return Response({
                    'status':True,
                    'Message':'Login success',
                    'data':{
                        # 'token':str(token)
                    }
                })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':'Something went wrong'
            })
  
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        data = {"logout": "logged out successfully"}
        return Response(data, status=status.HTTP_200_OK)

class Payment(APIView):
    def post(self,request):
        try:
            data=request.data
            serialise=PaymentDetailsSerialiser(data=data)
            if(serialise.is_valid()):
                serialise.save()
                return Response({"status":201,'pay':serialise.data,'message':'Payment has been successful'})
            else:
                return Response({'status':403,'error':serialise.errors,'message':'Invalid data'})
        except Exception as e:
            print(e)
            return Response({
                'status':404,
                'message':'Something went wrong',
                'data':{}
            })

class Package(APIView):
    def post(self,request):
        try:
            data=request.data
            serialiser=PackageSerialiser(data=data)
            if serialiser.is_valid():
                serialiser.save()
                return Response({
                    'status':201,
                    'message':'data has been save',
                    'data':{
                        'data':serialiser.data
                    }
                })
        except Exception as e:
            print(e)
            return Response({
                'status':404,
                'message':'Something went wrong',
                'data':{}
            })

class OtpVerify(APIView):
    def post(self,request):
        try:
            pass
        except Exception as e:
            print(e)
            return Response({
                'status':404,
                'message':'Something went wrong',
                'data':{}
            })



# class PersonalInfo(APIView):
#     def post(self,request):
#         serialiser=PersonalDetails(data=request.data)
#         if(serialiser.is_valid()):
#             serialiser.save()
#             return Response({'status':200,'message':"Personal details has been updated"})
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def patch(self,request):
#         try:
#             data=request.GET.get('pk')
#         # req=request.data
#             chek=PersonalInfo.objects.filter(mobile_number=data)
#             if not chek:
#                  return Response({"s tatus":403,'message':"Mobile number not found"})
#             serialise=PersonalDetailsSerialiser(chek,data=request.data,partial=True)
#             print(serialise)
#             if(serialise.is_valid()):
#                 serialise.save()
#                 return Response({'status':201,'message':"Data has been updated successfully"})
#             else:
#                 return Response({'status':404,'error':serialise.data,'message':"Data Invalid"})
#         except Exception as e:
#             print(e)
#             return Response({'status':400,'message':'Something went wrong'})