"""Tests for admin of refactoring app"""

from django.contrib.admin import ModelAdmin
from django.test import tag, TestCase

from refactoring.admin import RefactoringRecommendationAdmin


@tag("refactoring_admin")
class RefactoringRecommendationAdminTests(TestCase):
    """Test RefactoringRecommendationAdmin class"""

    def test_list_display(self) -> None:
        """Test list_display attribute"""

        self.assertEqual(
            RefactoringRecommendationAdmin.list_display,
            ("user", "date", "code"),
        )

    def test_list_filter(self) -> None:
        """Test list_filter attribute"""

        self.assertEqual(RefactoringRecommendationAdmin.list_filter, ("user",))

    def test_mro(self) -> None:
        """Test model MRO"""

        self.assertIn(ModelAdmin, RefactoringRecommendationAdmin.mro())
