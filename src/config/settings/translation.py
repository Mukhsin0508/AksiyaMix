from django.conf import settings


LANGUAGE_CODE = 'uz'

gettext = lambda s: s

LANGUAGES = [
    ('de', 'Uzbek'),
    ('ru', 'Russian'),
    ('uz', 'Uzbek'),
    ('en', 'English'),
]

MODELTRNSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRNSLATION_LANGUAGE = ('ru', 'uz', 'en')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uz', 'de')
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'uz'

USE_I18N = True

LOCALE_PATHS = [
    settings.BASE_DIR / 'locale',
]