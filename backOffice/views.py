from rest_framework import generics
from .models import Products, Transaction
from .serializers import ProductsSerializer, UserSerializer, LogoutSerializer, TransactionSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SingleProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "pk"


class TransactionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
