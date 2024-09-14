from django.shortcuts import render
from rest_framework import generics
from .models import Feature, FeatureValue, DiscountFeature
from .serializers import FeatureSerializer, FeatureValueSerializer, DiscountFeatureSerializer

# ===== CRUD for the Future model =====
class CreateFutureAPIView(generics.ListCreateAPIView):
    queryset = Feature.objects.all()

    serializer_class = FeatureSerializer

class UpdateFutureAPIView(generics.UpdateAPIView):
    queryset = Feature.objects.all()

    serializer_class = FeatureSerializer

class RetrieveFutureAPIView(generics.RetrieveAPIView):
    queryset = Feature.objects.all()

    serializer_class = FeatureSerializer

class DeleteFutureAPIView(generics.DestroyAPIView):
    queryset = Feature.objects.all()

    serializer_class = FeatureSerializer


# ===== CRUD for the FeatureValue model =====
class CreateFeatureValueAPIView(generics.ListCreateAPIView):
    queryset = FeatureValue.objects.all()

    serializer_class = FeatureValueSerializer

class UpdateFeatureValueAPIView(generics.UpdateAPIView):
    queryset = FeatureValue.objects.all()

    serializer_class = FeatureValueSerializer

class RetrieveFeatureValueAPIView(generics.RetrieveAPIView):
    queryset = FeatureValue.objects.all()

    serializer_class = FeatureValueSerializer

class DeleteFeatureValueAPIView(generics.DestroyAPIView):
    queryset = FeatureValue.objects.all()

    serializer_class = FeatureValueSerializer


# ===== CRUD for the DiscountFeature model =====
class CreateDiscountFeatureAPIView(generics.ListCreateAPIView):
    queryset = DiscountFeature.objects.all()

    serializer_class = DiscountFeatureSerializer

class UpdateDiscountFeatureAPIView(generics.UpdateAPIView):
    queryset = DiscountFeature.objects.all()

    serializer_class = DiscountFeatureSerializer

class RetrieveDiscountFeatureAPIView(generics.RetrieveAPIView):
    queryset = DiscountFeature.objects.all()

    serializer_class = DiscountFeatureSerializer

class DeleteDiscountFeatureAPIView(generics.DestroyAPIView):
    queryset = DiscountFeature.objects.all()

    serializer_class = DiscountFeatureSerializer

