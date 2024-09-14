from http.client import responses
from locale import currency

import requests
from celery import shared_task
from django.core.cache import cache

from apps.general.models import CurrencyRate
from apps.discount.currency_choices import Currency


@shared_task
def get_currency():
    """ Get currency rate from cbu.uz
    Params: None
    Returns: Updated currency rate
    """
    cache_key = "currency_rate"
    currency_rate = cache.get(cache_key)

    if not currency_rate:
        response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
        response.raise_for_status()
        data = response.json()
        currency_rate = data["Rate"]

        cache.set(cache_key, currency_rate, timeout=86400)
        print("Currency rate has been updated")
    return currency_rate
