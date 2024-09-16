REST_FRAMEWORK = {
    'DATE_FORMAT': '%d.%.m.%Y',
    'DATETIME_FORMAT': '%d.%.m.%Y %H:%M',
    'DATETIME_INPUT_FORMATS': [
        '%d.%m.%Y %H:%M',
    ],
    'DATE_INPUT_FORMATS': [
        '%d.%m.%Y %H:%M',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}