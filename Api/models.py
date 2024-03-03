from django.db import models
from datetime import datetime,date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    status= models.CharField(max_length=100, default=False)

    def __str__(self) -> str:
        return self.title
    

class User(AbstractUser):
    username=models.CharField(max_length=100)
    email= models.EmailField(default="youssef@gmail.com",unique=True)
    password= models.CharField(max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

   
    def __str__(self) -> str:
        return self.email