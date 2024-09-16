from PIL import Image
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension

def validate_image_size(image, max_width, max_height, error_message):
    """ Validate image size """
    if not image:
        raise ValidationError("Provided file is not an image.")

    try:
        validate_image_file_extension(image)

        img = Image.open(image)
        if img.width > max_width or img.height > max_height:
            raise ValidationError(error_message)

    except (AttributeError, IOError):
        raise ValidationError("Invalid image file. Could not open the image.")

def parent_category_image_size(image):
    validate_image_size(image, 500, 250, "Image size should be 500x250")

def promotional_banner_size(promotional_banner):
    validate_image_size(promotional_banner, 1000, 500, "Image size should be 1000x500")

def discount_image_size(image):
    validate_image_size(image, 500, 500, "Image size should be 500x500")

def service_image_size(image):
    validate_image_size(image, 500, 500, "Image size should be 500x500")

def company_logo_size(logo):
    validate_image_size(logo, 100, 100, "Image size should be 100x100")