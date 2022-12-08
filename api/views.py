from coreapi.auth import TokenAuthentication
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, filters

from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer


def home_view(request):
    return JsonResponse({'success':True, 'message':'Welcome to our online shop'})


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # search function by this url http://127.0.0.1:8000/api/products/?search=Samsung
    search_fields = ['name', 'description', 'serial_num', 'manufacturer_name', ]
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        serializer.save()


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # search function by this url http://127.0.0.1:8000/api/category/?search=Tablet
    search_fields = ['name', 'code', 'description']
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        serializer.save()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





