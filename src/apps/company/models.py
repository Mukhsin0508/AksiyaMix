import random
import string

from django.db import models
from django.conf import settings

from apps.company.validators import *
from apps.general.image_size import promotional_banner_size , company_logo_size


def generate_unique_id():
    """ Generate unique id for the company """
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


class Company(models.Model):
    """ Company model """
    id_generate = models.CharField(unique = True,
                                   max_length = 8,
                                   editable = False,
                                   default = generate_unique_id,
                                   validators = [validate_unique_id]
                                    )
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    slogan = models.CharField( max_length=255 )
    logo = models.ImageField ( upload_to = 'company_logo/%Y/%m/%d/',
                               validators = [company_logo_size],
                               blank = True ,
                               null = True
                               )
    video = models.FileField(upload_to='company_video/%Y/%m/%d',
                             validators = [company_video_format, validate_video_size,
                                           validate_video_duration, validate_video_resolution,
                                           validate_video_aspect_ratio, validate_audio_track
                                           ],
                             blank=True,
                             null=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    contact_phone = models.CharField(max_length=255)
    balance = models.DecimalField ( max_digits = 30 , decimal_places = 1 , default = 0 )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='company_owner')

    rating5 = models.CharField(default='0', max_length=55)
    rating4 = models.CharField(default='0', max_length=55)
    rating3 = models.CharField(default='0', max_length=55)
    rating2 = models.CharField(default='0', max_length=55)
    rating1 = models.CharField(default='0', max_length=55)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    installment = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    website = models.URLField ( blank = True , null = True )
    description = models.TextField ( max_length = 500 , blank = True , null = True )
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE,
                                 related_name='company_category')
    preferred_payment = models.ForeignKey('payment.Payments', on_delete=models.CASCADE,
                                          related_name='companies_payment')

    total_sales = models.CharField(default=0, max_length=55)
    followers = models.CharField(default=0, max_length=55)
    is_followed = models.BooleanField(default=False) # if True, then user is following the company
    total_comments = models.CharField(default=0, max_length=55)
    total_likes = models.CharField(default=0, max_length=55)
    total_dislikes = models.CharField(default=0, max_length=55)
    promotional_banner = models.ImageField(upload_to='company_promotional_banner/',
                                           validators =[promotional_banner_size],
                                           blank=True,
                                           null=True
                                        )

    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.username



class CompanyLocation(models.Model):
    """ Company location model """
    company = models.ForeignKey ( 'Company' , on_delete = models.CASCADE ,
                                  related_name = 'company_locations' )

    region = models.CharField(max_length=55)
    district = models.CharField(max_length=55)
    address = models.CharField(max_length=255)

    def get_address(self):
        return {
            'region': self.region,
            'district': self.district,
            'street': self.address,
            'longitude': self.company.longitude,
            'latitude': self.company.latitude
        }



class CompanyTimeTable(models.Model):
    """ Company timetable model """
    week_days_choice = (
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
    )

    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='timetable')
    week_days = models.CharField(max_length=20, choices=week_days_choice)
    open_time = models.TimeField()
    close_time = models.TimeField()
    is_closed = models.BooleanField(default=False)



