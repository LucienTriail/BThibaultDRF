from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
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


class UpdateProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, obj_id):
        try:
            return Products.objects.get(id=obj_id)
        except (Products.DoesNotExist, ValidationError):
            raise status.HTTP_404_NOT_FOUND

    def put(self, request, *args, **kwargs):
        data = request.data
        instances = []
        for temp_dict in data:
            product_id = temp_dict['id']
            discount = temp_dict['discount']
            stock = temp_dict['stock']
            obj = self.get_object(product_id)
            obj.discount = discount
            obj.stock = stock
            obj.save()
            instances.append(obj)
        serializer = ProductsSerializer(instances, many=True)
        return Response(serializer.data)


class SingleProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = "pk"


class TransactionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
