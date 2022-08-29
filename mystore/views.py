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

        queryset = self._calculate_stats(date_end, date_start, metric)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(list(queryset), many=True)
        return Response(serializer.data)

    def _calculate_stats(self, date_end, date_start, metric):
        if metric == 'count':
            value_func = Count
            value_param = 'products'
        elif metric == 'price':
            value_func = Sum
            value_param = 'products__price'

        queryset = self.get_queryset()
        queryset = queryset.filter(date__range=(date_start, date_end))
        queryset = queryset.annotate(month=TruncMonth('date')) \
            .values('month') \
            .annotate(value=value_func(value_param), date=Cast(TruncMonth('date'), output_field=DateField())) \
            .values('month', 'value')

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

