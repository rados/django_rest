from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mystore import views

urlpatterns = [
    path('mystore/', views.Order.as_view()),
    path('mystore/<int:pk>/', views.Product.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
