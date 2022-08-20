"""Test services.utils module"""

from django.test import TestCase, tag

from refactoring.tests.constants import (
    CORRECT_SNAKE_CASE_STRINGS, INCORRECT_SNAKE_CASE_STRINGS,
    CORRECT_CAP_WORDS_STRINGS, INCORRECT_CAP_WORDS_STRINGS,
    VALID_CODES, INVALID_CODES_AND_ERROR, NOT_STRING_VALUES, CODE_AND_HTML_CODE
)
from refactoring.services.utils import (
    is_in_snake_case, is_in_cap_words, get_code_error,
    get_code_to_display_in_html, get_code_items_without_duplicates,
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

    def test_get_code_to_display_in_html(self) -> None:
        """Test get_code_to_display_in_html function"""

        for code, expected_code in CODE_AND_HTML_CODE.items():
            with self.subTest(f'{code=}'):
                self.assertEqual(
                    get_code_to_display_in_html(code),
                    expected_code
                )

        for value in NOT_STRING_VALUES:
            with self.subTest(f'{value=}'):
                self.assertEqual(get_code_to_display_in_html(value), value)

    def test_get_code_items_without_duplicates(self) -> None:
        """Test get_code_items_without_duplicates function"""

        not_list_or_tuple_value = 10_000

        self.assertEqual(
            get_code_items_without_duplicates(not_list_or_tuple_value),
            set(),
        )

        self.assertEqual(
            sorted(get_code_items_without_duplicates([10, 10.0, 12.0, 12])),
            sorted([12, 10.0]),
        )
