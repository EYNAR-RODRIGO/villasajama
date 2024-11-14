"""
WSGI config for SistemaWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('C:/Users/EYNAR_RODRIGO/Desktop/VILLA SAJAMA A/PROYECTO DJANGO/SistemaWeb')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SistemaWeb.settings')

application = get_wsgi_application()
