"""Tests services of refactoring app"""

from django.test import TestCase, tag

from refactoring.tests.constants import (
    CORRECT_SNAKE_CASE_STRINGS, INCORRECT_SNAKE_CASE_STRINGS,
)
from refactoring.services.utils import is_in_snake_case


@tag('refactoring_services', 'refactoring_services_utils')
class ServicesUtilsTests(TestCase):
    """Test utils from services"""

    def test_is_in_snake_case(self) -> None:
        """Test is_in_snake_case function"""

        for string in INCORRECT_SNAKE_CASE_STRINGS:
            with self.subTest(f'{string=}'):
                self.assertFalse(is_in_snake_case(string))

        for string in CORRECT_SNAKE_CASE_STRINGS:
            with self.subTest(f'{string=}'):
                self.assertTrue(is_in_snake_case(string))
