from django.contrib import admin
from django.apps import apps
from mystore.models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    raw_id_fields = ('products',)

admin.site.register(Order, OrderAdmin)
