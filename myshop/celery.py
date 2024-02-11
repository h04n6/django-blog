import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')

# By setting the CELERY namespace, all CELERY settings need to include the CELERY_ prefix in their name
# For example, CELERY_BROKER_URL
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery will look for a 'tasks.py' in each application directory of applications added to the
# INSTALLED_APPS in order to load asynchronous tasks defined in it.
app.autodiscover_tasks()
