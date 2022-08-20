from mystore.models import Product, Order
from mystore.serializers import ProductSerializer, OrderSerializer
from rest_framework import generics


class Order(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

