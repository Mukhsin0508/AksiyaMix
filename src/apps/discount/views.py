from rest_framework import generics, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import *
from .serializers import *



# ===== CRUD for the DiscountTypes model =====
class DiscountTypesListCreateView(generics.ListCreateAPIView):
    queryset = DiscountTypes.objects.all()
    serializer_class = DiscountTypesSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DiscountTypesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiscountTypes.objects.all()
    serializer_class = DiscountTypesSerializer

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ===== CRUD for the Discount model =====
class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DiscountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)