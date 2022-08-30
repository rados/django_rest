from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mystore import views

urlpatterns = [
    path('api/products/<int:pk>/', views.ProductViewSet.as_view()),
    path('api/orders/<int:pk>/', views.OrderViewSet.as_view()),
    path('api/stats/', views.StatsViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
