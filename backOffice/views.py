from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SingleProduct(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "pk"


