"""Models of refactoring app"""

from django.contrib.auth import get_user_model
from django.db import models


class RefactoringRecommendation(models.Model):
    """Refactoring recommendation that user saved"""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )

    code = models.TextField(
        'исходный код',
        max_length=10_000,
    )

    recommendation = models.TextField(
        'рекомендация по рефакторингу',
    )

    date = models.DateTimeField(
        'дата рефакторинга',
        auto_now_add=True,
    )

    class Meta:
        """Info of RefactoringRecommendation model"""

        verbose_name = 'Рекомендация по рефакторингу'

        verbose_name_plural = 'Рекомендации по рефакторингу'

        ordering = ['-date']
