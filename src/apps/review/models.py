from django.db import models
from django.conf import settings


class Reviews(models.Model):
    """ Reviews model for company reviews"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    review = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CompanyVerified(models.Model):
    """ Company Verified model"""
    status_choices = (
        ('submitted', 'submitted'),
        ('in_process', 'in_process'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )
    status = models.CharField(max_length=255, choices=status_choices, default='submitted')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='company_verified')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


