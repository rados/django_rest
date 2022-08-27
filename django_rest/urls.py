"""sampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mystore.views import OrderViewSet, ProductViewSet, StatsViewSet
from rest_framework.routers import DefaultRouter


# Routers provide an easy way of automatically determining the URL conf.

router = DefaultRouter()
router.register(r'api/orders', OrderViewSet, basename='order')
router.register(r'api/products', ProductViewSet, basename='product')
router.register(r'api/stats', StatsViewSet, basename='order')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    # path(
    #     '^api/stats/(?P<metric>[price|count])(?P<start_date>\d{4}-\d{2}-\d{2})(?P<end_date>\d{4}-\d{2}-\d{2})$',
    #     StatsViewSet
    # ),
]
