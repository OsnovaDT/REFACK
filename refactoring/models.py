"""Models of refactoring app"""

from django.contrib.auth import get_user_model
from django.db import models


class RefactoringRecommendation(models.Model):
    """Saved user's refactoring recommendations"""

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    code = models.TextField(
        max_length=10_000,
    )

    recommendation = models.TextField()

    date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        """Metainformation about RefactoringRecommendation model"""

        verbose_name = 'Рекомендация по рефакторингу'

        verbose_name_plural = 'Рекомендации по рефакторингу'

        ordering = ['-date']
