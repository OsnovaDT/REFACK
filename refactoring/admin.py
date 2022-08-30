"""Admin panel of refactoring app"""

from django.contrib.admin import ModelAdmin, register

from refactoring.models import RefactoringRecommendation


@register(RefactoringRecommendation)
class RefactoringRecommendationAdmin(ModelAdmin):
    """Admin panel for RefactoringRecommendation model"""

    list_display = ("user", "date", "code")

    list_filter = ("user",)
