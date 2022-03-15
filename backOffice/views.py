from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Products, Transaction
from .serializers import ProductsSerializer, TransactionSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SingleProduct(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "pk"

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer





