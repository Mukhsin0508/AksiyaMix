from django.contrib.auth  import get_user_model

def get_sentinel_user():
    """Return the deleted user"""
    return get_user_model().objects.get_or_create(username='deleted')[0]