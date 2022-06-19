"""Config of refactoring app"""

from django.apps import AppConfig


class RefactoringConfig(AppConfig):
    """Config class"""

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'refactoring'
