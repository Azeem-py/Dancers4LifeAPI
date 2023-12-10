from rest_framework import serializers
from .models import *

class DanceSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = DanceClass
  
  fields = '__all__'
  
  extra_kwargs = {
            
            "name": {"required": True},
            "description": {"required": True},
            "slogan": {"required": True},
            "startDate": {"required": True},
            "endDate": {"required": True},
            "price": {"required": True},
           
        }

 def create(self, validated_data):
  newClass = DanceClass.objects.create(**validated_data)
  newClass.save()
  return newClass
 
class CardDanceSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = DanceClass
  
  fields = ('id','price','name', 'slogan', 'featureImg', 'startDate', 'endDate')
 

class EventSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = Event
  
  fields = '__all__'
  
  extra_kwargs = {
            
            "name": {"required": True},
            "description": {"required": True},
            "slogan": {"required": True},
            "startDate": {"required": True},
            "endDate": {"required": True},
            "price": {"required": True},
            
        }

 def create(self, validated_data):
  newEvent = Event.objects.create(**validated_data)
  newEvent.save()
  return newEvent

class CardEventSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = Event
  
  fields = ('id','name','price', 'slogan', 'featureImg', 'date')
  
  
class EnrollSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = Enrollment
  
  fields = '__all__'
  
  extra_kwargs = {
            
            "user": {"required": True},
            "DanceClass": {"required": True},
  
        }

 def create(self, validated_data):
  newEnroll = Enrollment.objects.create(**validated_data)
  newEnroll.save()
  return newEnroll

class TicketSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = Ticket
  
  fields = ('email', 'event')
  
  extra_kwargs = {
            
            "email": {"required": True},
            "event": {"required": True},
  
        }

 def create(self, validated_data):
  newTicket = Ticket.objects.create(**validated_data)
  newTicket.save()
  return newTicket