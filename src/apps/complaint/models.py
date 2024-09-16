from click.core import batch
from django.db import models
from django.conf import settings

from apps.user.validators import phone_validate


class Complaint(models.Model):
    """ Complaint model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null = True,
                             related_name='complaints'
                             )
    company = models.ForeignKey('company.Company',
                                on_delete=models.SET_NULL,
                                blank = True,
                                null = True,
                                related_name='complaints')
    discount = models.ForeignKey('discounts.Discount',
                                 on_delete=models.CASCADE,
                                 blank = True,
                                 null = True,
                                 related_name='complaints')

    title = models.CharField(max_length=55)
    text = models.TextField(max_length = 200)
    phone_number = models.CharField(max_length = 13, validators = [phone_validate], blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.phone_number:
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return  self.phone_number