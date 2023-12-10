# models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=60)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return str(self.id)
       
    def verify(self):
      self.is_verified = True
      self.save()
    
    def update_password(self, password):
     self.set_password(password)
     self.save()
     
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='customuser_set',
    #     related_query_name='customuser',
    #     blank=True,
    #     verbose_name='groups',
    # )
    
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='customuser_set',
    #     related_query_name='customuser',
    #     blank=True,
    #     verbose_name='user permissions',
    # )
       
class OTPModel(models.Model):
 user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
 otp = models.IntegerField(blank=False)
 datetime = models.DateTimeField(auto_now_add=True)
 used = models.BooleanField(default=False)
 
 # def update_used(self):
 #  self.used = True
 #  self.save()
 
 def __str__(self):
  return self.user.email
 
