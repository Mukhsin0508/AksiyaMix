from django.db import models

class Feature(models.Model):
    """ Feature model"""
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

class FeatureValue(models.Model):
    """ Feature Value model"""
    feature = models.ForeignKey('Feature', on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=255)

class DiscountFeature(models.Model):
    discount = models.ForeignKey('discount.Discount', on_delete=models.CASCADE, related_name='discount_features')
    feature_value = models.ForeignKey('FeatureValue', on_delete=models.CASCADE, related_name='discount_values')
    ordering_number = models.PositiveSmallIntegerField(default=0)
    price = models.FloatField()
    old_price = models.FloatField()
