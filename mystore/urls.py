from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mystore import views

urlpatterns = [
    path('api/products/<int:pk>/', views.Product.as_view()),
    path('api/products/', views.ProductList.as_view()),
    path('api/orders/', views.OrderList.as_view()),
    path('api/orders/<int:pk>/', views.Order.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
