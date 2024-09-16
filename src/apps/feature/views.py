from rest_framework import generics
from .models import Feature, FeatureValue, DiscountFeatureCombination, DiscountFeatureValue
from .serializers import FeatureSerializer, FeatureValueSerializer, DiscountFeatureSerializer




# ===== CRUD for the Future model =====
class FeatureListCreateView(generics.ListCreateAPIView):
    queryset = Feature.objects.all()

    serializer_class = FeatureSerializer

class FeatureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()

    serializer_class = FeatureSerializer



# ===== CRUD for the FeatureValue model =====
class FeatureValueListCreateView(generics.ListCreateAPIView):
    queryset = FeatureValue.objects.all()

    serializer_class = FeatureValueSerializer

class FeatureValueRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeatureValue.objects.all()

    serializer_class = FeatureValueSerializer



# ===== CRUD for the DiscountFeature model =====
class DiscountFeatureCombinationListCreateView(generics.ListCreateAPIView):
    queryset = DiscountFeatureCombination.objects.all()

    serializer_class = DiscountFeatureSerializer

class DiscountFeatureCombinationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiscountFeatureCombination.objects.all()

    serializer_class = DiscountFeatureSerializer



# ===== CRUD for the DiscountFeature model =====
class DiscountFeatureValueListCreateView(generics.ListCreateAPIView):
    queryset = DiscountFeatureValue.objects.all()

    serializer_class = DiscountFeatureSerializer

class DiscountFeatureValueRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiscountFeatureValue.objects.all()

    serializer_class = DiscountFeatureSerializer

