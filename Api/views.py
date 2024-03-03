from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django.contrib.auth import authenticate, login
from django.urls import reverse
from rest_framework.authentication import authenticate, SessionAuthentication
from rest_framework import serializers,status
from django.contrib.auth.hashers import make_password
from . serlializers import TodoSerializer, UserSerialiser
# Create your views here.

@api_view(['GET'])
def Apiviews(request):
    api_url={
        'index': '/',
        'add':'/create',
        'update': '/update/pk',
        'delete':'todo/pk/delete'
    }
    return Response(api_url)

#cree un todo
@api_view(['POST','GET'])
def views_item(request):
    item= TodoSerializer(data=request.data)
    if Todo.objects.filter(**request.data).exists():
        raise serializers.ValidationError("""{"title": "dfghjk", "description": "zertyjé"}""")
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#afficher tout
@api_view(['GET'])
def afficher_all(request):
    if request.query_params:
        item= Todo.objects.filter(**request.query_params.dict())
    else:
        item = Todo.objects.all()
    if item:
        serializer= TodoSerializer(item, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

#mise a jour
    
@api_view(['GET', 'POST'])
def updates(request, pk):
    item= Todo.objects.get(pk=pk)
    data= TodoSerializer(instance=item, data= request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["GET","POST"])

def delete(request,pk):
    items= get_object_or_404(Todo, pk=pk)
    items.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(["POST"])
def sing(request):
        user= UserSerialiser(data=request.data)
        if User.objects.filter(email=request.data.get("email")).exists():
            raise serializers.ValidationError("""il exist déja {"email": "dfghjk", "password": "zertyjé"}""")
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["POST","GET"])
def loging(request):
    username=request.data.get("username")
    email=request.data.get("email")
    password=make_password("password").encode("utf-8")
    #password = request.data.get("password")
    user= authenticate(request, email=email, password=password)
    print(user)
    print(username)
    print(email)
    print(password)
    if user:
         login(request, user)
    # user_auth=authenticate(request, username=user.username, email=user.email)
         return Response({"message": "success"})
    else:
        return Response({"error": " email ou password Invalid"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
def all_to(request):
    item = User.objects.all()
    data= UserSerialiser(item, many=True)
    return Response(data.data)
    