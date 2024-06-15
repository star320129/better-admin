import os
import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
django.setup()


app = Celery('main_celery')

