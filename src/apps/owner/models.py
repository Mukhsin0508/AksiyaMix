from django.db import models
from apps.user.validators import phone_validate, email_validate

class Owner(models.Model):
    """ Owner model"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique = True, editable = False)
    phone_number = models.CharField(max_length=255, validators = [phone_validate])
    profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m/%d', blank=True, null=True)
    email = models.EmailField(max_length=255,
                              validators = [email_validate],
                              unique = True,
                              blank = True)

    created_at = models.DateTimeField(auto_now_add=True)

    def generate_username(self):
        """ Generate username from first_name """
        return f'@{self.first_name.lower()}'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.generate_username()
        super().save(*args, **kwargs)

