"""Tests for the app"""

from django.test import TestCase

from refactoring.code_inspector import (
    is_bool_function_correct, is_get_function_correct,
)
from refactoring.tests.constants import (
    CORRECT_BOOL_FUNCTIONS, INCORRECT_BOOL_FUNCTIONS, BOOL_FUNCTION_TYPE,
    CORRECT_GET_FUNCTIONS, INCORRECT_GET_FUNCTIONS, GET_FUNCTION_TYPE,
    DIFFERENT_VALUES,
)


class CodeInspectorTests(TestCase):
    """Tests for code_inspector.py module"""

    def test_is_bool_function_correct(self):
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
        for value in DIFFERENT_VALUES:
            with self.subTest(value):
                self.assertFalse(
                    is_bool_function_correct('is_correct', value)
                )

    def test_is_get_function_correct(self):
        """Test is_get_function_correct function"""

        # Check correct function name
        for function in CORRECT_GET_FUNCTIONS:
            with self.subTest(function):
                self.assertTrue(
                    is_get_function_correct(function, GET_FUNCTION_TYPE)
                )

        # Check incorrect function name
        for function in INCORRECT_GET_FUNCTIONS:
            with self.subTest(function):
                self.assertFalse(
                    is_get_function_correct(function, GET_FUNCTION_TYPE)
                )

        # Check incorrect get function type
        for value in DIFFERENT_VALUES:
            with self.subTest(value):
                self.assertFalse(
                    is_bool_function_correct('get_value', value)
                )
