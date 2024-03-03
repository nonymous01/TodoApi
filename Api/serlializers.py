from django.db.models import fields
from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields=('title','description','status')

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=('username','email','password')


    
