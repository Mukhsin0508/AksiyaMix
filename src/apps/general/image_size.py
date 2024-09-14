from PIL import Image
from django.core.exceptions import ValidationError

def validate_image_size(image, max_width, max_height, error_message):
    try:
        img = Image.open(image)
        if img.width > max_width or img.height > max_height:
            raise ValidationError(error_message)
    except AttributeError:
        raise ValidationError("Invalid image file.")

def parent_category_image_size(image):
    validate_image_size(image, 500, 250, "Image size should be 500x250")

def promotional_banner_size(promotional_banner):
    validate_image_size(promotional_banner, 1000, 500, "Image size should be 1000x500")

def discount_image_size(image):
    validate_image_size(image, 500, 500, "Image size should be 500x500")

def service_image_size(image):
    validate_image_size(image, 500, 500, "Image size should be 500x500")
