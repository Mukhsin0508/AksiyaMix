from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings.base')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'refresh-currency-every-midnight': {
        'task': 'apps.general.tasks.get_currency',
        'schedule': crontab(hour='0', minute='1')
    },
}

@app.task(bind=True)
def debug_task(self):
    print( f'Request: {self.request!r}' )