from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import serializers,status
from . serlializers import TodoSerializer
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
    