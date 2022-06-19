"""Test code_inspector.py from refactoring app"""

from django.test import TestCase

from refactoring.code_inspector import (
    is_bool_function_correct, is_get_function_correct,
)
from refactoring.tests.constants import (
    BOOL_FUNCTION_TYPE, GET_FUNCTION_TYPE, DIFFERENT_VALUES,
    CORRECT_BOOL_FUNCTIONS, INCORRECT_BOOL_FUNCTIONS,
    CORRECT_GET_FUNCTIONS, INCORRECT_GET_FUNCTIONS,
)


class CodeInspectorTests(TestCase):
    """Tests for code_inspector.py"""

    def test_is_bool_function_correct(self) -> None:
        """Test is_bool_function_correct function"""

        # Check correct function name
        for function in CORRECT_BOOL_FUNCTIONS:
            with self.subTest(function):
                self.assertTrue(
                    is_bool_function_correct(function, BOOL_FUNCTION_TYPE)
                )

        # Check incorrect function name
        for function in INCORRECT_BOOL_FUNCTIONS:
            with self.subTest(function):
                self.assertFalse(
                    is_bool_function_correct(function, BOOL_FUNCTION_TYPE)
                )

        # Check incorrect bool function type
        for type_ in DIFFERENT_VALUES:
            with self.subTest(type_):
                self.assertFalse(
                    is_bool_function_correct('is_correct', type_)
                )

    def test_is_get_function_correct(self) -> None:
        """Test is_get_function_correct function"""

        # Check correct function name
        for function in CORRECT_GET_FUNCTIONS:
            with self.subTest(f'{function=}'):
                self.assertTrue(
                    is_get_function_correct(function, GET_FUNCTION_TYPE)
                )

        # Check incorrect function name
        for function in INCORRECT_GET_FUNCTIONS:
            with self.subTest(f'{function=}'):
                self.assertFalse(
                    is_get_function_correct(function, GET_FUNCTION_TYPE)
                )

        # Check incorrect get function type
        for type_ in DIFFERENT_VALUES:
            with self.subTest(f'{type_=}'):
                self.assertFalse(
                    is_bool_function_correct('get_value', type_)
                )
