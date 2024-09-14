from django.db import  models

class Currency(models.IntegerChoices):
    """ Currency model"""
    USD = 1, 'USD'
    UZS = 2, 'UZS'