from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreateDiscountTypeAPIView.as_view(), name='discount_create'),
    path('retrieve/<int:pk>/', RetrieveDiscountTypeAPIView.as_view(), name='discount_retrieve'),
    path('update/<int:pk>/', UpdateDiscountTypeAPIView.as_view(), name='discount_update'),
    path('delete/<int:pk>/', DeleteDiscountTypeAPIView.as_view(), name='discount_delete'),

    path('create/', CreateDiscountAPIView.as_view(), name='discount_create'),
    path('retrieve/<int:pk>/', RetrieveDiscountAPIView.as_view(), name='discount_retrieve'),
    path('update/<int:pk>/', UpdateDiscountAPIView.as_view(), name='discount_update'),
    path('delete/<int:pk>/', DeleteDiscountAPIView.as_view(), name='discount_delete'),

]