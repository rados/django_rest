from mystore.models import Product, Order
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']
        extra_kwargs = {'orders': {'required': False}}


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'date', 'products']
        extra_kwargs = {'products': {'required': False}}
