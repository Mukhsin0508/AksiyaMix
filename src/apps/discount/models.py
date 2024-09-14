from django.db import models
from polymorphic.models import PolymorphicModel
from .currency_choices import Currency
from apps.general.image_size import discount_image_size, service_image_size


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

    id_generate = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    product_id = models.IntegerField()

    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='discounts')
    branch = models.ManyToManyField('branch.Branch', related_name='discounts', blank=True)

    price = models.PositiveSmallIntegerField(choices=Currency.choices, default='UZS')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)  # if True, then the discount is active
    currency = models.CharField(max_length=3, choices=Currency.choices, default='UZS')

    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='discounts')
    features = models.ManyToManyField('feature.Feature', related_name='discounts')

    created_at = models.DateTimeField(auto_now_add=True)
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


# Subclass models
class StandardDiscount(Discount):
    """ Standard discount model, like 10% off """
    discount_value = models.FloatField()
    discount_value_is_percent = models.BooleanField(default=True)


class BundleDiscount(Discount):
    """ Free product discount model, like buy 1, get 1 free """
    min_quantity = models.IntegerField()
    bonus_quantity = models.IntegerField()


class QuantityDiscount(Discount):
    """ Quantity discount model, like 10% off on 10 items """
    min_quantity = models.IntegerField()
    bonus_discount_value = models.FloatField()
    bonus_discount_value_is_percent = models.BooleanField(default=True)


class ServiceDiscount(Discount):
    """ Service discount model, like 10% off on delivery """
    min_quantity = models.IntegerField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='discounts_services')


class DiscountImage(models.Model):
    """ Discount image model """
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='discount_images')
    image = models.ImageField(upload_to='discounts/images', validators=[discount_image_size])


class Service(models.Model):
    """ Service model for creating services """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='discount/services/icons')


class ServiceImage(models.Model):
    """ Service image model """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_images')
    image = models.ImageField(upload_to='discounts/services/images', validators=[service_image_size])
