"""Tests for config of refactoring app"""

from django.test import tag, TestCase

from config.tests.constants import DEFAULT_AUTO_FIELD
from refactoring.apps import RefactoringConfig


@tag("refactoring_config")
class RefactoringConfigTests(TestCase):
    """Test RefactoringConfig class"""

    def test_default_auto_field(self) -> None:
        """Test default_auto_field attribute"""

        self.assertEqual(
            RefactoringConfig.default_auto_field,
            DEFAULT_AUTO_FIELD,
        )

    def test_name(self) -> None:
        """Test name attribute"""

        self.assertEqual(RefactoringConfig.name, "refactoring")
