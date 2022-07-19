"""Test admin of refactoring app"""

from django.contrib.admin import ModelAdmin
from django.test import TestCase, tag

from refactoring.admin import RefactoringRecommendationAdmin


@tag('refactoring_admin')
class RefactoringRecommendationAdminTests(TestCase):
    """Test RefactoringRecommendationAdmin class"""

    def test_list_display(self) -> None:
        """Test list_display attribute"""

        self.assertEqual(
            RefactoringRecommendationAdmin.list_display,
            ('user', 'code', 'recommendation', 'date'),
        )

    def test_list_filter(self) -> None:
        """Test list_filter attribute"""

        self.assertEqual(
            RefactoringRecommendationAdmin.list_filter, ('user',)
        )

    def test_model_admin_in_mro(self) -> None:
        """Test that ModelAdmin in RefactoringRecommendationAdmin MRO"""

        self.assertIn(ModelAdmin, RefactoringRecommendationAdmin.mro())
