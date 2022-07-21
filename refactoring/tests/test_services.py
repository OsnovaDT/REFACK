"""Tests services of refactoring app"""

from django.test import TestCase, tag

from refactoring.tests.constants import (
    CORRECT_SNAKE_CASE_STRINGS, INCORRECT_SNAKE_CASE_STRINGS,
    CORRECT_CAP_WORDS_STRINGS, INCORRECT_CAP_WORDS_STRINGS,
    INVALID_CODE_AND_ERROR, VALID_CODE, NOT_STRING_VALUES,
)
from refactoring.services.utils import (
    is_in_snake_case, is_in_cap_words, get_error_if_code_invalid,
)


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

    def test_is_in_cap_words(self) -> None:
        """Test is_in_cap_words function"""

        for string in INCORRECT_CAP_WORDS_STRINGS:
            with self.subTest(f'{string=}'):
                self.assertFalse(is_in_cap_words(string))

        for string in CORRECT_CAP_WORDS_STRINGS:
            with self.subTest(f'{string=}'):
                self.assertTrue(is_in_cap_words(string))

    def test_get_error_if_code_invalid(self) -> None:
        """Test get_error_if_code_invalid function"""

        for code, expected_error in INVALID_CODE_AND_ERROR.items():
            self.assertEqual(get_error_if_code_invalid(code), expected_error)

        for value in VALID_CODE + NOT_STRING_VALUES:
            self.assertEqual(get_error_if_code_invalid(value), '')
