
from .celery import app as celery_app

__all__ = ("celery_app",)

# celery -A djangoProject4 worker -l info --pool=solo       : command to start celery server on windows