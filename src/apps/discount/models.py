import random
import string

from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.cache import cache
from polymorphic.models import PolymorphicModel
from .currency_choices import Currency
from apps.general.image_size import discount_image_size, service_image_size
from apps.discount.validators import *


def generate_unique_id():
    """ Generate unique id for the company """
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


class DiscountTypes(models.Model):
    """ Discount types like standard, bundle, quantity, service """
    DISCOUNT_TYPE_CHOICES = [
        ('standard', 'Standard'),  # discounts like 10% off
        ('bundle', 'Bundle'),  # discounts like buy 1, get 1 free
        ('quantity', 'Quantity'),  # discounts like 10% off on 10 items
        ('service', 'Service'),    # discounts like 10% off on delivery
    ]
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPE_CHOICES, default='standard', unique=True)


class Discount(PolymorphicModel):
    """ Discount model, base class for polymorphic inheritance """
    status_choices = (
        ('submitted', 'submitted'),
        ('in_process', 'in_process'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )

    id_generate = models.CharField(unique = True,
                                   max_length = 8,
                                   editable = False,
                                   default = generate_unique_id,
                                   validators = [validate_unique_id]
                                    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    product_id = models.IntegerField()

    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='discounts')
    branch = models.ManyToManyField('branch.Branch', related_name='discounts', blank=True)

    price = models.PositiveSmallIntegerField(choices=Currency.choices, default='UZS')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)  # if True, then the discount is active
    currency = models.CharField(max_length=3, choices=Currency.choices, default='UZS')

    category = models.ForeignKey('category.Category',
                                 on_delete=models.PROTECT,
                                 related_name='discounts',
                                 limit_choices_to = {"parent__parent__isnull": False}
                                 )
    features = models.ManyToManyField('feature.Feature', related_name='discounts')

    video = models.FileField(upload_to='discounts/videos/%Y/%m/%d',
                             validators = [discount_video_format, validate_video_size,
                                           get_video_duration, validate_video_duration,
                                           validate_video_resolution, validate_video_aspect_ratio,
                                           get_video_audio_channels, validate_audio_track
                                           ],
                             blank=True,
                             null=True
                             )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_stock = models.BooleanField(default=True)  # if True, then the product is in stock
    is_popular = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    available_in_stock = models.IntegerField(default=0)
    is_delivery = models.BooleanField(default=False)
    is_installment = models.BooleanField(default=False)

    # Status by admin on (MultipleChoice, submitted, in_process, approved/rejected)
    status = models.CharField(max_length=20, choices=status_choices, default='submitted')
    is_favorite = models.BooleanField(default=False)

    is_viewed = models.BooleanField(default=False)  # if True, then @user has viewed the discount
    views = models.PositiveSmallIntegerField(default=0)
    likes = models.PositiveSmallIntegerField(default=0)
    dislikes = models.PositiveSmallIntegerField(default=0)
    comments = models.ForeignKey('comment.DiscountComments',
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='discounts_comments')

    # Discount types like standard, bundle, quantity, service
    discount_type = models.ForeignKey('DiscountTypes', on_delete=models.CASCADE, related_name='discounts_types')


    def get_currency_rate(self):
        """ Fetch the currency rate from the cache """
        cache_key = "currency_rate"
        return cache.get(cache_key)

    def get_price_in_currency(self, currency):
        """ Convert and return the price in the cached currency rate """
        if currency == self.currency:
            return self.price

        rate = self.get_currency_rate()
        if rate:
            base_currency = self.currency
            base_price = self.price

            converted_price = base_price / rate
            return  converted_price

        return None

    def get_old_price_in_currency(self, currency):
        """ Convert and return the old price based on the cached currency rate """
        if currency == self.currency:
            return self.old_price

        rate = self.get_currency_rate()
        if rate:
            base_currency = self.currency
            base_old_price = self.old_price

            converted_old_price = base_old_price / rate
            return converted_old_price

        return None

    def clean(self):
        super ( ).clean ( )

        # Common validations for all discount types
        if self.start_date >= self.end_date:
            raise ValidationError ({'start_date': "Start date must be before end date"})

        if self.end_date <= timezone.now():
            raise ValidationError ({'end_date': "End date must be in the future"})

        # Type-specific validations
        discount_type = self.discount_type.discount_type if self.discount_type else None

        if discount_type == 'standard':
            self._validate_standard_discount()
        elif discount_type == 'bundle':
            self._validate_bundle_discount()
        elif discount_type == 'quantity':
            self._validate_quantity_discount()
        elif discount_type == 'service':
            self._validate_service_discount()

    def _validate_standard_discount(self):
        if not hasattr (self, 'standarddiscount'):
            return

        if not self.standarddiscount.discount_value:
            raise ValidationError({'discount_value': "Discount value is required"})

        if self.standarddiscount.discount_value_is_percent:
            if self.standarddiscount.discount_value < 1 or self.standarddiscount.discount_value > 99:
                raise ValidationError({'discount_value': "Discount value must be between 1 and 99 percent"})

    def _validate_bundle_discount(self):
        if not hasattr(self, 'bundlediscount'):
            return

        if not self.bundlediscount.min_quantity:
            raise ValidationError({'min_quantity': "Min quantity is required"})

        if not self.bundlediscount.bonus_quantity:
            raise ValidationError({'bonus_quantity': "Bonus quantity is required"})

    def _validate_quantity_discount(self):
        if not hasattr(self, 'quantitydiscount'):
            return

        if not self.quantitydiscount.min_quantity:
            raise ValidationError({'min_quantity': "Min quantity is required"})

        if not self.quantitydiscount.bonus_discount_value:
            raise ValidationError({'bonus_discount_value': "Bonus discount value is required"})

        if self.quantitydiscount.bonus_discount_value_is_percent:
            if self.quantitydiscount.bonus_discount_value < 1 or self.quantitydiscount.bonus_discount_value > 99:
                raise ValidationError(
                    {'bonus_discount_value': "Bonus discount value must be between 1 and 99 percent"} )

    def _validate_service_discount(self):
        if not hasattr (self,'servicediscount'):
            return

        if not self.servicediscount.min_quantity:
            raise ValidationError({'min_quantity': "Min quantity is required"})

        if not self.servicediscount.service:
            raise ValidationError({'service': "Service is required"})

    def save(self , *args , **kwargs):
        if not self.id_generate:
            self.id_generate = generate_unique_id()
            self.full_clean()
        super ().save(*args , **kwargs)

    def __str__(self):
        return self.title


# Subclass models
class StandardDiscount(Discount):
    """ Standard discount model, like 10% off """
    discount_value = models.DecimalField(max_digits = 20, decimal_places = 1, blank = True, null = True)
    discount_value_is_percent = models.BooleanField(default=True)


class BundleDiscount(Discount):
    """ Free product discount model, like buy 1, get 1 free """
    min_quantity = models.PositiveSmallIntegerField(blank = True, null = True)
    bonus_quantity = models.PositiveSmallIntegerField(blank = True, null = True)


class QuantityDiscount(Discount):
    """ Quantity discount model, like 10% off on 10 items """
    min_quantity = models.PositiveSmallIntegerField(blank = True, null = True)
    bonus_discount_value = models.DecimalField(max_digits = 20, decimal_places = 1, blank = True, null = True)
    bonus_discount_value_is_percent = models.BooleanField(default=True)


class ServiceDiscount(Discount):
    """ Service discount model, like 10% off on delivery """
    min_quantity = models.PositiveSmallIntegerField(blank = True, null = True)
    service = models.ForeignKey('Service',
                                on_delete=models.SET_NULL,
                                blank = True,
                                null = True,
                                related_name='discounts_services'
                                )


class DiscountImage(models.Model):
    """ Discount image model """
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='discount_images')
    image = models.ImageField(upload_to='discounts/images/%Y/%m/%d', validators=[discount_image_size])
    ordering_number = models.PositiveSmallIntegerField(default=0)


class Service(models.Model):
    """ Service model for creating services """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    icon = models.ImageField(upload_to='discount/services/icons/%Y/%m/%d', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self , **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super().save()


class ServiceImage(models.Model):
    """ Service image model """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_images')
    image = models.ImageField(upload_to='discounts/services/images/%Y/%m/%d', validators=[service_image_size])
