from rest_framework import serializers, validators
from .models import *


class SignUpSerializer(serializers.ModelSerializer):
 class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

 def create(self, validated_data):
     user = CustomUser(
         email=validated_data['email'],
         name=validated_data['name']
     )
     user.set_password(validated_data['password'])
     user.save()
     return user

class UserIDSerializer(serializers.ModelSerializer):
 class Meta:
        model = CustomUser
        fields = ('id',)

 


class OTPSerializer(serializers.ModelSerializer):
 class Meta:
  model = OTPModel
  
  fields = '__all__'
  
 def create(self, validated_data):
  otp = OTPModel.objects.create(**validated_data)
  otp.save()
  return otp
  