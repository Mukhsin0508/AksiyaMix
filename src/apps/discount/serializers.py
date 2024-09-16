from rest_framework import serializers

from .models import (Discount, DiscountTypes, StandardDiscount, BundleDiscount, QuantityDiscount,
                     ServiceDiscount, DiscountImage, Service, ServiceImage)
from apps.comment.models import DiscountComments



class DiscountCommentsSerializer(serializers.ModelSerializer):
    """ Discount comments serializer """

    class Meta:
        model = DiscountComments
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    """ Discount serializer """

    class Meta:
        model = Discount
        fields = '__all__'


class DiscountTypesSerializer(serializers.ModelSerializer):
    """ Discount types serializer """

    class Meta:
        model = DiscountTypes
        fields = '__all__'


class StandardDiscountSerializer(serializers.ModelSerializer):
    """ Standard discount serializer """

    class Meta:
        model = StandardDiscount
        fields = '__all__'


class BundleDiscountSerializer(serializers.ModelSerializer):
    """ Bundle discount serializer """

    class Meta:
        model = BundleDiscount
        fields = '__all__'


class QuantityDiscountSerializer(serializers.ModelSerializer):
    """ Quantity discount serializer """

    class Meta:
        model = QuantityDiscount
        fields = '__all__'


class ServiceDiscountSerializer(serializers.ModelSerializer):
    """ Service discount serializer """

    class Meta:
        model = ServiceDiscount
        fields = '__all__'


class DiscountImageSerializer(serializers.ModelSerializer):
    """ Discount image serializer """

    class Meta:
        model = DiscountImage
        fields = '__all__'


class ServiceImageSerializer(serializers.ModelSerializer):
    """ Service image serializer """

    class Meta:
        model = ServiceImage
        fields = '__all__'
