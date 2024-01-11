# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeliveryGranada.settings')
app = Celery('DeliveryGranada')

# Configuración de Celery con settings de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre las tareas en la aplicación Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
