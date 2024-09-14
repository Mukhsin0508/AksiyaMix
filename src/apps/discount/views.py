from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *



# ===== CRUD for the DiscountTypes model =====
class CreateDiscountTypeAPIView(generics.ListCreateAPIView):
    queryset = DiscountTypes.objects.all()

    serializer_class = DiscountTypesSerializer

class RetrieveDiscountTypeAPIView(generics.RetrieveAPIView):
    queryset = DiscountTypes.objects.all()

    serializer_class = DiscountTypesSerializer

class UpdateDiscountTypeAPIView(generics.UpdateAPIView):
    queryset = DiscountTypes.objects.all()

    serializer_class = DiscountTypesSerializer

class DeleteDiscountTypeAPIView(generics.DestroyAPIView):
    queryset = DiscountTypes.objects.all()

    serializer_class = DiscountTypesSerializer


# ===== CRUD for the Discount model =====
class CreateDiscountAPIView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()

    serializer_class = DiscountSerializer

class RetrieveDiscountAPIView(generics.RetrieveAPIView):
    queryset = Discount.objects.all()

    serializer_class = DiscountSerializer

class UpdateDiscountAPIView(generics.UpdateAPIView):
    queryset = Discount.objects.all()

    serializer_class = DiscountSerializer

class DeleteDiscountAPIView(generics.DestroyAPIView):
    queryset = Discount.objects.all()

    serializer_class = DiscountSerializer