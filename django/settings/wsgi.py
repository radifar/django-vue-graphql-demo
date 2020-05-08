"""
WSGI config for django_vue project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
project_folder = os.path.expanduser(PROJECT_DIR)
load_dotenv(os.path.join(PROJECT_DIR, '.env'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

application = get_wsgi_application()
