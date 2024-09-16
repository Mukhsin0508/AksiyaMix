from django.core.exceptions import ValidationError
from email_validator import validate_email, EmailNotValidError


def phone_validate(phone_number: str) -> None:
    if not isinstance(phone_number, str):
        phone_number = str(phone_number)

    if len(phone_number) !=13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('Invalid phone number format. Please enter a phone number in the format +998XXXXXXXXX')


def email_validate(email: str) -> None:
    try:
        email_info = validate_email(email, check_deliverability=False)
        email = email_info.normalized
    except EmailNotValidError as e:
        raise ValidationError(str(e))