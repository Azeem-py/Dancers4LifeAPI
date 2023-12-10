from rest_framework.response import Response
from rest_framework import views, viewsets, generics, status, permissions
from .serializers import *

class DanceClassView(viewsets.ViewSet):
 def create(self, request):
  data = request.data
  serializer = DanceSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)

 def class_data(self, request, card=None):
   query = DanceClass.objects.all()
   serializerClass = CardDanceSerializer if card == 1 else DanceSerializer
   serializer = serializerClass(query, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)
 
 
class EventView(viewsets.ViewSet):
 def create(self, request):
  data = request.data
  serializer = EventSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)
 
 def event_data(self, request, card=None):
   query = Event.objects.all()
   serializerClass = CardEventSerializer if card == 1 else EventSerializer
   serializer = serializerClass(query, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)
 

class EnrollView(viewsets.ViewSet):
 permission_classes = (permissions.IsAuthenticated,)
 def create(self, request):
  data = request.data
  serializer = EnrollSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)

class TicketView(viewsets.ViewSet):
 def create(self, request):
  data = request.data
  serializer = TicketSerializer(data=data)
  serializer.is_valid(raise_exception=True)
  serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)

 def list(self, request):
  query = Ticket.objects.all()
  serializer = TicketSerializer(query, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)