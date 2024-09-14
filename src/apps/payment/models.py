from django.db import models

class Payments(models.Model):
    """ Payment model
    :arg models.Model: Django model
    :returns: Payment model
    """
    title = models.CharField(max_length=255) # title of the payment
    price = models.FloatField() # price of the payment
    currency = models.PositiveSmallIntegerField() # currency of the payment
    created_at = models.DateTimeField(auto_now_add=True) # date of the payment creation

    def __str__(self):
        return self.title