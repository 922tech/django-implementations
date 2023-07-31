
"""Celery implementatinos"""
import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject4.settings")
app = Celery("djangoProject4")
app.config_from_object("django.conf:settings", namespace="CELERY")

# This line makes celery to look for a task.py file in each django app
# Alternative: add a CELERY_IMPORTS to configurations in settings.py manually
app.autodiscover_tasks()