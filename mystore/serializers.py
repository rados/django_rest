from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Order, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Product
        fields = ['id', 'title', 'price']


class OrderSerializer(WritableNestedModelSerializer):
    products = ProductSerializer(many=True, allow_null=True)
    class Meta:
        ordering = ['-id']
        model = Order
        fields = ['id', 'date', 'products']
        extra_kwargs = {'products': {'required': False}}


class StatsSerializer(serializers.Serializer):
    value = serializers.IntegerField()
    month = serializers.DateField(format='%Y %b')

