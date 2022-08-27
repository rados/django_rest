from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from mystore.models import Product, Order
from mystore.serializers import ProductSerializer, OrderSerializer
from rest_framework import generics
from rest_framework import filters


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

