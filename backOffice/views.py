from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


class ProductList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SingleProduct(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "pk"


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
