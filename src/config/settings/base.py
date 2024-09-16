import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from .jazzmin import JAZZMIN_SETTINGS



load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY=os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
INTERNAL_IPS = os.getenv("INTERNAL_IPS").split(",")
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS") == "True"

INSTALLED_APPS = [
    "jazzmin" , # which is used to add the admin panel # pip install jazzmin
    "modeltranslation" , # which is used to translate the models # pip install django-modeltranslation

    "django.contrib.admin" ,
    "django.contrib.auth" ,
    "django.contrib.contenttypes" ,
    "django.contrib.sessions" ,
    "django.contrib.messages" ,
    "django.contrib.staticfiles" ,

    "django_ckeditor_5" , # which is used to add rich text editor # pip install django-ckeditor
    # 'ckeditor', # which is used to add rich text editor # pip install django-ckeditor
    'ckeditor_uploader', # which is used to upload the images in the rich text editor # pip install django-ckeditor-uploader
    "django_celery_beat" , # which is used to schedule the tasks # pip install django-celery-beat
    "django_celery_results" , # which is used to store the results of the tasks # pip install django-celery-results
    "corsheaders" , # which is used to allow given host to access the resources # pip install django-cors-headers
    "rest_framework" , # which is used to create the restful api # pip install djangorestframework
    "rest_framework.authtoken" , # which is used to create the token based authentication # pip install djangorestframework
    "debug_toolbar" , # which is used to debug the application # pip install django-debug-toolbar
    "drf_yasg" , # which is used to create the api documentation # pip install drf-yasg

    'apps.ads.apps.AdsConfig',
    'apps.authentication.apps.AuthenticationConfig',
    'apps.branch.apps.BranchConfig',
    'apps.category.apps.CategoryConfig',
    'apps.comment.apps.CommentConfig',
    'apps.company.apps.CompanyConfig',
    'apps.complaint.apps.ComplaintConfig',
    'apps.discount.apps.DiscountConfig',
    'apps.feature.apps.FeatureConfig',
    'apps.general.apps.GeneralConfig',
    'apps.notification.apps.NotificationConfig',
    'apps.owner.apps.OwnerConfig',
    'apps.payment.apps.PaymentConfig',
    'apps.review.apps.ReviewConfig',
    'apps.search.apps.SearchConfig',
    'apps.user.apps.UserConfig',
    'apps.wishlist.apps.WishlistConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True # which is used to enable the internationalization
USE_TZ = True # which is used to enable the timezone

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

CKEDITOR_UPLOAD_PATH = "uploads/%Y/%m/%d/"
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_DATE = True


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

