import requests

GET_TEMPLATE_URL = "https://notify.eskiz.uz/api/user/templates"
GET_TOKEN_URL = "https://notify.eskiz.uz/api/auth/login"
SEND_SMS_URL = "https://notify.eskiz.uz/api/message/sms/send"  # Updated URL

FORGOT_PASSWORD_MESSAGE = "Parolingizni tiklash uchun quayside havolaga o'ting: {link}"
AUTH_CODE_MESSAGE = "WiderAI websaytiga kirish uchun tasdiqlash kodingiz: {code}"

EMAIL = "muxsinmuxtorov01@gmail.com"
PASSWORD = "foQfClYgA4XFMIIYrwKrsElW2cpZLiTb0akH2TUG"

# Get token
response = requests.post(
    url=GET_TOKEN_URL,
    data={
        'email': EMAIL,
        'password': PASSWORD
    }
)

if response.status_code == 200:
    response_data = response.json()
    TOKEN = response_data['data']['token']
    print(f"Token: {TOKEN}")

    # Get templates
    response = requests.get(
        url=GET_TEMPLATE_URL,
        headers={
            'Authorization': f"Bearer {TOKEN}"
        }
    )

    if response.status_code == 200:
        response_data = response.json()
        print("Templates:", response_data)
    else:
        print(f"Failed to get templates. Status code: {response.status_code}")
        print(f"Response: {response.text}")

    if TOKEN:
        # send sms
        response = requests.post(
            url=SEND_SMS_URL,
            headers={
                'Authorization': f"Bearer {TOKEN}"
            },
            data={
                'mobile_phone': '+998993233528',  # Added missing quote
                'message': 'WiderAI websaytiga kirish uchun tasdiqlash kodingiz: 1234',
                'from': '4546',
            }
        )
        if response.status_code == 200:
            response_data = response.json()
            print("SMS sent:", response_data)  # Changed response to response_data
        else:
            print(f"Failed to send SMS. Status code: {response.status_code}")
            print(f"Response: {response.text}")
else:
    print(f"Failed to get token. Status code: {response.status_code}")
    print(f"Response: {response.text}")