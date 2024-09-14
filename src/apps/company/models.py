from django.db import models
from django.conf import settings


class Company(models.Model):
    """ Company model """
    id_generate = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    contact_phone = models.CharField(max_length=255)

    address = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logo/', blank=True, null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company_owner')
    rating5 = models.CharField(default=0, max_length=55)
    rating4 = models.CharField(default=0, max_length=55)
    rating3 = models.CharField(default=0, max_length=55)
    rating2 = models.CharField(default=0, max_length=55)
    rating1 = models.CharField(default=0, max_length=55)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    slogan_uz = models.CharField( max_length=255 )
    slogan_ru = models.CharField(max_length=255)
    description_uz = models.TextField(max_length=1000)
    description_ru = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank=True, null=True)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='company_category')
    preferred_payment = models.ForeignKey('payment.Payments', on_delete=models.CASCADE, related_name='companies_payment')
    total_sales = models.CharField(default=0, max_length=55)
    followers = models.CharField(default=0, max_length=55)
    is_followed = models.BooleanField(default=False) # if True, then user is following the company
    total_comments = models.CharField(default=0, max_length=55)
    total_likes = models.CharField(default=0, max_length=55)
    total_dislikes = models.CharField(default=0, max_length=55)
    promotional_banner = models.ImageField(upload_to='company_promotional_banner/', blank=True, null=True)

    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)


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



