import  os
from  django.conf  import  settings

POSTGRES=True

if POSTGRES:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        }
    }
else:
    DATABASES = {
        "default":{
            "ENGINE": "django.db.backends.sqlite3" ,
            "NAME": settings.BASE_DIR /"db.sqlite3" ,
        }
    }
    print (DATABASES)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache" ,
        "LOCATION": "redis://redis:6379/2" ,
    }
}

