"""Models of refactoring app"""

from django.db import models
from django.contrib.auth import get_user_model


class UserRecomendation(models.Model):
    """Saved user's refactoring recommendations"""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    code = models.TextField(
        max_length=10_000,
    )

    recomendation = models.TextField()

    date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        """Metainformation about UserRecomendation model"""

        verbose_name = 'Рекомендации по рефакторингу'
