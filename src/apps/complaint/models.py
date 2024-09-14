from django.db import models
from django.conf import settings



class Complaint(models.Model):
    """ Complaint model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='complaints')
    branch = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, related_name='complaints',
                               blank=True, null=True)

    title = models.CharField(max_length=255)
    text = models.TextField()
    shared_phone = models.CharField(max_length=255) # phone number of the user retrieved from user's
                                                    # profile with user's consent to be shared with the company

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)