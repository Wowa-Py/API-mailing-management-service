import os
import time

from celery import Celery

# Переменная окружения для настроек Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maillind.settings')

# Экземпляр Celery
app = Celery('maillind')

# Загрузка настроек из файла settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL

# Автоматическое обнаружение и регистрация задач
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    print('Hello! Form debug_task! All ok!')
