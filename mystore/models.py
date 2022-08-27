from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        ordering = ['date']
