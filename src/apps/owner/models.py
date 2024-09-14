from django.db import models

class Owner(models.Model):
    """ Owner model"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)