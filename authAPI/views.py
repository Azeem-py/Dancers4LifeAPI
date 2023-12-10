from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import SignUpSerializer, OTPSerializer
from .otpGen import generate_otp
from .sendOTP import send_otp_email
from .models import CustomUser, OTPModel
from django.shortcuts import get_object_or_404
from django.utils import timezone

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
       
class GetID(viewsets.ViewSet):
  def getID(self,request):
    id = request.user.id
    return Response({'id': id})
  
class checkAuth(viewsets.ViewSet):
  permission_classes = (permissions.IsAuthenticated,)
  def isAuth(self, request):
    return Response({'isAuth': 'True'}, status=status.HTTP_202_ACCEPTED)
  
class SignUpView(viewsets.ViewSet):
 def create(self, request):
  data = request.data
  if data['password'] != data['password2']:
   return Response({'error':'Password fields don\'t match'})
  serializer = SignUpSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)
 
 def otp(self, request, id=None, email=None):
  if id:
   user = id
  else:
   user = CustomUser.objects.get(email=email).id
  otp = generate_otp()
  
  serializer = OTPSerializer(data={'otp': otp, 'user': user})
  serializer.is_valid(raise_exception=True)
  serializer.save()
  email = CustomUser.objects.get(id=user).email
  send_otp_email(email, otp)

  return Response(serializer.data, status=status.HTTP_201_CREATED)
 
 def verifyOTP(self, request, id, otp):
  user = get_object_or_404(CustomUser, id=id)
  latest_otp = OTPModel.objects.filter(user=id).last()
  print(latest_otp)
  
  if user.is_verified: return Response({'verified':'user has been verified already'})
  else:
   if otp == latest_otp.otp:
    if (timezone.now() - latest_otp.datetime).total_seconds() < 3600:
     user.verify()
     # latest_otp.update_used()
     return Response({"verify": 'verification complete'}, status=status.HTTP_200_OK)
    return Response({"Error": 'OTP Expired'}, status=status.HTTP_400_BAD_REQUEST)
   return Response({"Error": 'OTP not correct'}, status=status.HTTP_400_BAD_REQUEST)
  
 
 def reset_password(self,request):
  email = request.data['email']
  otp = request.data['otp']
  password = request.data['password']
  user = get_object_or_404(CustomUser, email=email)
  latest_otp = OTPModel.objects.filter(user=user.id).last()
  print(type(latest_otp), type(otp))
  if int(otp) == latest_otp.otp:
    if (timezone.now() - latest_otp.datetime).total_seconds() < 3600:
      user.update_password(password)
      return Response({'success': 'password reset successful'})
    
    else: return Response({'error': 'otp expired'})
  else: return Response({'error': 'otp not valid'})

  
   
   
   
 
   

  