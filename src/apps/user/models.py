from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

from apps.user.managers import CustomUserManager
from apps.user.validators import phone_validate , birthdate_validate


class CustomUser(AbstractUser):
    """ Custom User model"""
    class Gender(models.IntegerChoices):
        MAN = 1, 'Мужчина'
        WOMAN = 2, 'Женщина'

    groups = models.ManyToManyField(Group, related_name='customUser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customUser_set_permissions')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    USERNAME_FIELD = 'phone_number'
    username = models.CharField(max_length=255, unique = True)
    object = CustomUserManager()

    phone_number = models.CharField(max_length=13, unique=True, validators=[phone_validate])

    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, blank=True, null=True)

    birth_date = models.DateField(validators = [birthdate_validate], blank = True, null = True)
    address = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ('phone_number', 'username')

    def __str__(self):
        return self.phone_number

    def generate_username(self):
        """ Generate username from first_name """
        return f'@{self.first_name.lower()}'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.generate_username()
        super().save(*args, **kwargs)


class UserLocation(models.Model):
    """ Company location model """
    company = models.ForeignKey ( 'CustomUser' , on_delete = models.CASCADE ,
                                  related_name = 'user_locations' )

    region = models.CharField(max_length=55)
    district = models.CharField(max_length=55)

    def get_user_address(self):
        return {
            'region': self.region,
            'district': self.district,
        }

class UserToken(models.Model):
    """ User Token model"""
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='tokens')
    access_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'access_token')

    def __str__(self):
        return self.access_token
