"""Config file of account app"""

from django.apps import AppConfig


class AccountConfig(AppConfig):
    """Config class of account app"""

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'account'
