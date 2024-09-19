import requests
import random
import json

from asgiref.timeout import timeout
from django.conf import settings
from django.core.cache import cache


class EskizUz:
    TOKEN_KEY = "eskiz_uz_token"
    AUTH_CODE_KEY = "auth_code_{username}"

    GET_TOKEN_URL = "https://notify.eskiz.uz/api/auth/login"
    SEND_SMS_URL = "https://notify.eskiz.uz/api/message/sms/send"

    FORGOT_PASSWORD_MESSAGE = "Parolingizni tiklash uchun quayside havolaga o'ting: {link}"
    AUTH_CODE_MESSAGE = "WiderAI websaytiga kirish uchun tasdiqlash kodingiz: {code}"

    EMAIL = settings.ESKIZ_UZ_EMAIL
    PASSWORD = settings.ESKIZ_UZ_PASSWORD

    @classmethod
    def get_token(cls):
        token = cache.get(cls.TOKEN_KEY)
        if not token:
            response = requests.post(
                url = cls.GET_TOKEN_URL,
                json = {
                    'email': cls.EMAIL,
                    'password': cls.PASSWORD
                }
            )
            response.raise_for_status()
            token = response.json()['data']['token']

            cache.set(cls.TOKEN_KEY, token, timeout=60 * 60 * 24 * 29)
        return token

    @classmethod
    def send_sms(cls, username: str, message_type: str, nickname: str = '4546', link=None) -> None:
        if message_type == "FORGOT_PASSWORD":
            message =  cls.FORGOT_PASSWORD_MESSAGE.format(link = link)
        elif message_type == "AUTH_CODE":
            code = random.randint( 1000, 9999 )
            message = cls.AUTH_CODE_MESSAGE.format(code = code)
            cache.set(cls.AUTH_CODE_KEY.format(username = username), code, timeout = 60 * 10 )
        else:
            raise ValueError("Invalid message type, message type must be FORGOT_PASSWORD or AUTH_CODE")

        headers = {
            'Authorization': f"Bearer {
            cls.get_token()}",
        }
        data = {
            'mobile_phone': username,
            'message': message,
            'from': nickname
        }
        response = requests.post(url= cls.SEND_SMS_URL, headers=headers, json=data)

        if response.status_code == 401:
            cache.delete(cls.TOKEN_KEY)
            headers = {
                'Authorization': f"Bearer {
                cls.get_token()}" ,
            }

            requests.post ( url = cls.SEND_SMS_URL , headers=headers , json=data )

