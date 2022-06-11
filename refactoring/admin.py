"""Admin panel for refactoring app"""

from django.contrib import admin

from refactoring.models import UserRecomendation


@admin.register(UserRecomendation)
class UserRecomendationAdmin(admin.ModelAdmin):
    """Admin for UserRecomendation model"""

    list_display = ('user', 'code', 'recomendation', 'date')

    list_filter = ('user',)
