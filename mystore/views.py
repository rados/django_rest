from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.db.models.functions import TruncDay, TruncDate, TruncMonth, TruncYear, TruncWeek, Cast, ExtractMonth
from django.db.models import DateField, Count, Sum
from .serializers import OrderSerializer, ProductSerializer, StatsSerializer
from .models import Product, Order
from rest_framework import filters

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class StatsViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = StatsSerializer

    def list(self, request, *args, **kwargs):
        date_start = request.GET.get('date_start', None)
        date_end = request.GET.get('date_end', None)
        metric = request.GET.get('metric', None)

        if metric not in ['count', 'price']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset()  # self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(date__range=(date_start, date_end))

        #todo: add switch statement
        if metric == 'count':
            queryset = queryset.annotate(month=TruncMonth('date')) \
                .values('month') \
                .annotate(value=Count('products'), date=Cast(TruncMonth('date'), output_field=DateField())) \
                .values('month', 'value')
        elif metric == 'price':
            queryset = queryset.annotate(month=TruncMonth('date')) \
                .values('month') \
                .annotate(value=Sum('products__price'), date=Cast(TruncMonth('date'), output_field=DateField())) \
                .values('month', 'value')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(list(queryset), many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

