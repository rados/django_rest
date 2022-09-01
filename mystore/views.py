from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models.functions import TruncMonth, Cast
from django.db.models import DateField, Count, Sum
from django.utils.dateparse import parse_date
from .serializers import OrderSerializer, ProductSerializer, StatsSerializer
from .models import Product, Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class StatsViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Order.objects.all()
    serializer_class = StatsSerializer


    def list(self, request, *args, **kwargs):
        date_start = request.GET.get('date_start', None)
        date_end = request.GET.get('date_end', None)
        metric = request.GET.get('metric', None)

        if date_start is None or date_end is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )

        if parse_date(date_start) is None or parse_date(date_end) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if metric == 'count':
            metric_func = Count
            metric_param = 'products'
        elif metric == 'price':
            metric_func = Sum
            metric_param = 'products__price'
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = self._calculate_stats(date_end, date_start, metric_func, metric_param)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(list(queryset), many=True)
        return Response(serializer.data)

    def _calculate_stats(self, date_end, date_start, metric_func, metric_param):

        queryset = self.get_queryset()
        queryset = queryset.filter(date__range=(date_start, date_end))
        queryset = queryset.annotate(month=TruncMonth('date')) \
            .values('month') \
            .annotate(value=metric_func(metric_param), date=Cast(TruncMonth('date'), output_field=DateField())) \
            .values('month', 'value')

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

