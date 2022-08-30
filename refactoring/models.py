"""Models of refactoring app"""

from django.contrib.auth import get_user_model
from django.db import models


class RefactoringRecommendation(models.Model):
    """Refactoring recommendation saved by user"""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    code = models.TextField(
        'Исходный код',
        max_length=10_000,
    )

    recommendation = models.TextField(
        'Рекомендация по рефакторингу',
    )

    date = models.DateTimeField(
        'Дата рефакторинга',
        auto_now_add=True,
    )

    class Meta:
        """Meta info for RefactoringRecommendation model"""

        verbose_name = 'Рекомендация по рефакторингу'
        verbose_name_plural = 'Рекомендации по рефакторингу'

        ordering = ['-date']
