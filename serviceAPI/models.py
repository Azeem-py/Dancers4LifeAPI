from django.db import models
from authAPI.models import CustomUser

# Create your models here.

class DanceClass(models.Model):
 name = models.CharField(max_length=30, blank=False)
 slogan = models.CharField(max_length=80, blank=False)
 description = models.TextField(max_length=5000)
 startDate = models.DateField(blank=False, )
 endDate = models.DateField(blank=False)
 featureImg = models.ImageField(blank=True, upload_to='images/')
 price = models.FloatField(blank=False)

 
 def __str__(self) -> str:
   return self.name
 
class Event(models.Model):
 name = models.CharField(max_length=60, blank=False)
 slogan = models.CharField(max_length=80, blank=False)
 description = models.TextField(max_length=5000)
 date = models.DateField(blank=False, )
 featureImg = models.ImageField(upload_to='images/', blank=True)
 price = models.FloatField(blank=False)
 
 
 def __str__(self):
     return self.name
    
class Enrollment(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  DanceClass = models.ForeignKey(DanceClass, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  
  def __str__(self) -> str:
    return f'{self.DanceClass.name} {self.user.name}'
  
class Ticket(models.Model):
  email = models.EmailField(blank=False)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)

  
  def __str__(self) -> str:
    return self.event.name
  

   
 
