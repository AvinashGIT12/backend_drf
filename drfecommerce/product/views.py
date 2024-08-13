from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . serializers import *
from drf_spectacular.utils import extend_schema
# Create your views here.
from . models import *

class CategoryView(viewsets.ViewSet):
    queryset=Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list (self,request):
        serializer_category=CategorySerializer(self.queryset,many=True)
        return Response(serializer_category.data)
    
class BrandView(viewsets.ViewSet):
    queryset=Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list (self,request):
        serializer_brand=BrandSerializer(self.queryset,many=True)
        return Response(serializer_brand.data)
    

class ProductView(viewsets.ViewSet):
    queryset=Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list (self,request):
        serializer_product=ProductSerializer(self.queryset,many=True)
        return Response(serializer_product.data)
    
