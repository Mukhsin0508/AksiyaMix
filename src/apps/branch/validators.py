from apps.branch.models import Branch
from django.core.exceptions import ValidationError
from apps.branch.models import generate_unique_id


def validate_unique_id(value):
    """ Validate unique id for the company """

    max_attempts = 100
    attempts = 0

    while Branch.objects.filter(id_generate = value).exists():
        if attempts >= max_attempts:
            raise  ValidationError("Unable to generate a unique ID, Please try again! ")
        value = generate_unique_id()
        attempts += 1

    return value
