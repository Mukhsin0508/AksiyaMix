from django.db import models
from django.conf import  settings


class Wishlist(models.Model):
    """ Wishlist model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlists')
    discount = models.ForeignKey('discount.Discount', on_delete=models.CASCADE, related_name='wishlists')
    added_at = models.DateTimeField(auto_now_add=True)