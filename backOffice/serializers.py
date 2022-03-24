from requests import Response
from rest_framework import serializers, status
from .models import Products, Transaction
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(TransactionSerializer, self).__init__(many=many, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     many = True if isinstance(request.data, list) else False
    #     serializer = TransactionSerializer(data=request.data, many=many)
    #     serializer.is_valid(raise_exception=True)
    #     author = request.user  # you can change here
    #     book_list = [Transaction(**data,author=author) for data in serializer.validated_data]
    #     Transaction.objects.bulk_create(book_list)
    #     return Response({}, status=status.HTTP_201_CREATED)

    class Meta:
        model = Transaction
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
