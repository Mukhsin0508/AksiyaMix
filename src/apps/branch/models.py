import random
import string

from django.db import models

from apps.company.validators import validate_unique_id
from apps.general.normalizer import normalizer_text
from apps.company.models import Company


def generate_unique_id():
    """ Generate unique id for the company """
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


class Branch(models.Model):
    """ Branch model"""
    id_generate = models.CharField(unique = True,
                                   max_length = 8,
                                   editable = False,
                                   default = generate_unique_id,
                                   validators = [validate_unique_id]
                                    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    is_delivery = models.BooleanField(default=False)

    longitude = models.FloatField()
    latitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('company', 'name')

    def save(self, *args, **kwargs):
        normalizer_text(self)
        super().save(*args, **kwargs)



class BranchLocation(models.Model):
    """ Company location model """
    branch = models.ForeignKey ( 'Branch' , on_delete = models.CASCADE ,
                                  related_name = 'branch_locations' )

    region = models.CharField(max_length=55)
    district = models.CharField(max_length=55)
    address = models.CharField(max_length=255)

    def get_branch_address(self):
        return {
            'region': self.region,
            'district': self.district,
            'street': self.address,
            'longitude': self.branch.longitude,
            'latitude': self.branch.latitude
        }

class BranchTimeTable(models.Model):
    """ Branch Time Table model"""
    DAY_CHOICES = (
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    )
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='timetables')
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        unique_together = ('branch', 'day')