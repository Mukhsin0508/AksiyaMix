from django.db import models
from apps.general.normalizer import normalizer_text
from apps.company.models import Company


class Branch(models.Model):
    """ Branch model"""
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