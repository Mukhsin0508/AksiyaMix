from django.db import models
from django.core.exceptions import ValidationError

class Feature(models.Model):
    """ Feature model"""
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='features')
    measure_type = models.CharField(max_length=20, blank=True)  # like 'cm', 'kg', 'grams'
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        unique_together = (('category', 'slug'),)

    def __str__(self):
        return self.title

class FeatureValue(models.Model):
    """ Feature Value model"""
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.feature.title}: {self.value}"

class DiscountFeatureCombination(models.Model):
    """ Model to store price for specific feature combinations """
    discount = models.ForeignKey('discount.Discount', on_delete=models.CASCADE, related_name='feature_combinations')
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Combination for {self.discount.title}"

    def clean(self):
        if self.price >= self.old_price:
            raise ValidationError("Discounted price must be less than the old price.")

class DiscountFeatureValue(models.Model):
    """ Model to link feature values to a specific combination """
    combination = models.ForeignKey(DiscountFeatureCombination, on_delete=models.CASCADE, related_name='feature_values')
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('combination', 'feature_value')

    def __str__(self):
        return f"{self.combination.discount.title} - {self.feature_value}"

    @staticmethod
    def get_price_for_combination(discount , feature_values):
        combination = DiscountFeatureCombination.objects.filter (
            discount = discount ,
            feature_values__feature_value__in = feature_values
        ).annotate (
            match_count = models.Count ( 'feature_values' )
        ).filter (
            match_count = len ( feature_values )
        ).first ( )

        return combination.price if combination else None