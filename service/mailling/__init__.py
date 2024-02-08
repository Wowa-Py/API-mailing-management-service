# from . import tasks
from .celery_config.py import app as celery_app

__all__ = ('celery_app',)
