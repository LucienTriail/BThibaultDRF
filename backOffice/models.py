from django.db import models


# Create your models here.

class Products(models.Model):
    discount = models.IntegerField()
    name = models.CharField(max_length=32)
    comments = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    category = models.IntegerField()
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    unit = models.CharField(max_length=24)
    sale = models.BooleanField(default=False)
    stock = models.IntegerField()
    sold = models.IntegerField()


class Transaction(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    productQuantity = models.IntegerField()
    category = models.CharField(max_length=32,default='empty')