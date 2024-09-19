from string import digits , ascii_letters

from django.core.exceptions import ValidationError
from email_validator import validate_email, EmailNotValidError
from datetime import datetime

import re
from string import ascii_lowercase , ascii_uppercase , digits , punctuation


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

def birthdate_validate(birth_date) -> None:
        try:
            datetime.strptime ( birth_date , '%d/%m/%Y' )
        except ValueError:
            raise ValueError ( "Incorrect data format, should be YYYY-MM-DD" )


def password_validate(password: str) -> tuple[bool , str]:
    """
    Validate the password against several criteria.

    Args:
    password (str): The password to validate

    Returns:
    tuple[bool, str]: A tuple containing a boolean (True if valid, False if not)
                      and a string message explaining the result
    """

    min_length = 8
    required_chars = [
        (ascii_lowercase , "lowercase letter") ,
        (ascii_uppercase , "uppercase letter") ,
        (digits , "digit") ,
        (punctuation , "special character")
    ]

    # Check length
    if len ( password ) < min_length:
        return False , f"Password must be at least {min_length} characters long."

    # Check for required character types
    missing = []
    for char_set , char_type in required_chars:
        if not any ( char in char_set for char in password ):
            missing.append ( char_type )

    if missing:
        return False , f"Password must contain at least one {', '.join ( missing )}."

    # Check for common patterns (optional)
    if re.search ( r'(.)\1{2,}' , password ):
        return False , "Password should not contain repeated characters (3 or more times in a row)."

    # If all checks pass
    return True , "Password is valid."