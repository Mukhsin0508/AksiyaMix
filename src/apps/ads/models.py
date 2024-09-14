from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from ..discount.models import Discount

class Advertisement(models.Model):
    """ Advertisement model """
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired'),
    ]
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, related_name='ads', null=True)

    title = models.CharField(max_length=255)
    description = CKEditor5Field()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    view_count = models.IntegerField(default=0)
    ad_price = models.FloatField()
    num_of_boost = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)