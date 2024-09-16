from http.client import responses
from locale import currency

import requests
from celery import shared_task
from django.core.cache import cache

@shared_task
def get_currency():
    """ Get currency rate from cbu.uz
    Params: None
    Returns: Updated currency rate
    """
    cache_key = "currency_rate"
    currency_rate = cache.get(cache_key)

    if not currency_rate:
        """ Get currency rate from cbu.uz
        Params: None
        Returns: Updated currency rate
        """
        try:
            response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
            response.raise_for_status()
            data = response.json()

            currency_rate = None

            if isinstance(data, list):
                for usd_currency in data:
                        if usd_currency["Ccy"] == "USD":
                            currency_rate = usd_currency.get("Rate")
                            break
            if currency_rate is None:
                print("USD currency rate not found in the response")


            cache.set(cache_key, currency_rate, timeout=86400)
            print("Currency rate has been updated" if currency_rate else "Currency rate has not been updated")

        except requests.RequestException as e:
            print(f"Error while getting currency rate: {e}")

    return currency_rate
