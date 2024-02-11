from .celery import app as celery_app

# Import the Celery module to ensure it is loaded when Django starts.
__all__ = ['celery_app']
