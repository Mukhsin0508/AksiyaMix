from rest_framework import serializers

from .models import Feature, FeatureValue, DiscountFeatureCombination, DiscountFeatureValue

# ====== Serializers for the Feature model, the FeatureValue model, and the DiscountFeature model ======

class FeatureSerializer(serializers.ModelSerializer):
    """ Feature serializer """

    class Meta:
        model = Feature
        fields = '__all__'


class FeatureValueSerializer(serializers.ModelSerializer):
    """ Feature Value serializer """

    class Meta:
        model = FeatureValue
        fields = '__all__'

class DiscountFeatureCombinationSerializer(serializers.ModelSerializer):
    """ Discount Feature Combination serializer """

    class Meta:
        model = DiscountFeatureCombination
        fields = '__all__'

class DiscountFeatureSerializer(serializers.ModelSerializer):
    """ Discount Feature serializer """

    class Meta:
        model = DiscountFeatureValue
        fields = '__all__'
