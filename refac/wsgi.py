"""WSGI config of project"""

from os import environ

from django.core.wsgi import get_wsgi_application


environ.setdefault('DJANGO_SETTINGS_MODULE', 'refac.settings')

application = get_wsgi_application()
