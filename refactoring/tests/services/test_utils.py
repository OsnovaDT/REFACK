"""Test services.utils module"""

from django.test import TestCase, tag

from refactoring.tests.constants import (
    CORRECT_SNAKE_CASE_STRINGS, INCORRECT_SNAKE_CASE_STRINGS,
    CORRECT_CAP_WORDS_STRINGS, INCORRECT_CAP_WORDS_STRINGS,
    VALID_CODES, INVALID_CODES_AND_ERROR, NOT_STRING_VALUES
)
from refactoring.services.utils import (
    is_in_snake_case, is_in_cap_words, get_code_error,
)


@tag('refactoring_services', 'refactoring_services_utils')
class UtilsTests(TestCase):
    """Test services.utils module"""

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

    def test_get_code_error(self) -> None:
        """Test get_code_error function"""

        for code in VALID_CODES + NOT_STRING_VALUES:
            with self.subTest(f'{code=}'):
                self.assertEqual(get_code_error(code), '')

        for code, error in INVALID_CODES_AND_ERROR.items():
            with self.subTest(f'{code=}'):
                self.assertEqual(get_code_error(code), error)
