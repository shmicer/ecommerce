import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_spam_every_5_min': {
        'task': 'account.tasks.send_beat_email',
        'schedule': crontab(minute='*/5'),
    },
}