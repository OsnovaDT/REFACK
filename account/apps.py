"""Config of account app"""

from django.apps import AppConfig


class AccountConfig(AppConfig):
    """Config class"""

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'account'
