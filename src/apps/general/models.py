from django.db import models
from apps.discount.currency_choices import Currency

class CurrencyRate(models.Model):
    currency = models.PositiveSmallIntegerField(choices=Currency.choices, unique=True)
    in_sum = models.DecimalField(max_length=20, decimal_places=3, max_digits=20)
    in_usd = models.DecimalField(max_length=20, decimal_places=3, max_digits=20)

    def __str__(self):
        return f"{self.currency} - {self.in_sum}"