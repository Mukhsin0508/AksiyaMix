from django.db import models
from django.conf import settings

class DiscountComments(models.Model):
    """ Discount comments model """
    discount = models.ForeignKey('discount.Discount', on_delete=models.CASCADE, related_name='comments_discount')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)