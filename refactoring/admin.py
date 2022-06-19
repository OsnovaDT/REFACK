"""Admin panel of refactoring app"""

from django.contrib.admin import ModelAdmin, register

from refactoring.models import RefactoringRecommendation


@register(RefactoringRecommendation)
class RefactoringRecommendation(ModelAdmin):
    """Admin for RefactoringRecommendation model"""

    list_display = ('user', 'code', 'recommendation', 'date')

    list_filter = ('user',)
