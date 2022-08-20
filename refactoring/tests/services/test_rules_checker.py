"""Test services.rules_checker module"""

from django.test import TestCase, tag

from refactoring.services.rules_checker import CleanCodeRulesChecker
from refactoring.tests.constants import (
    ARGUMENT_TYPE_HINT, CLASSES_WITHOUT_DOCSTRING, CLASS_DOCSTRING,
    CLASSES_WITH_DOCSTRING, CORRECT_SNAKE_CASE_FUNCTIONS,
    INCORRECT_SNAKE_CASE_FUNCTIONS, FUNCTIONS_WITH_ARGS,
    FUNCTION_TYPE_HINT, FUNCTIONS_WITHOUT_DOCSTRING,
    FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT_ERRORS, FUNCTIONS_WITH_TYPE_HINT,
    FUNCTIONS_WITHOUT_TYPE_HINT, FUNCTIONS_WITH_DOCSTRING, FUNCTION_DOCSTRING,
    SNAKE_CASE_STYLE, CAP_WORDS_STYLE, CORRECT_CAP_WORDS_CLASSES,
    INCORRECT_CAP_WORDS_CLASSES, CORRECT_GET_FUNCTIONS,
    INCORRECT_GET_FUNCTIONS, CORRECT_BOOL_FUNCTIONS, INCORRECT_BOOL_FUNCTIONS,
    PREFIX_GET, PREFIX_IS,
)


@tag('refactoring_services', 'refactoring_services_rules_checker')
class TypeHintCheckerMixinTests(TestCase):
    """Test TypeHintCheckerMixin mixin"""

    def test_check_functions_args_have_type_hints(self) -> None:
        """Test _check_functions_args_have_type_hints method"""

        rules_checker = CleanCodeRulesChecker({
            'functions': FUNCTIONS_WITH_ARGS,
        })

        rules_checker._check_functions_args_have_type_hints()

        self.assertEqual(
            sorted(rules_checker._recommendations[ARGUMENT_TYPE_HINT]),
            FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT_ERRORS,
        )

    def test_check_functions_have_type_hint(self) -> None:
        """Test _check_functions_have_type_hint method"""

        rules_checker = CleanCodeRulesChecker({
            'functions':
                FUNCTIONS_WITH_TYPE_HINT + FUNCTIONS_WITHOUT_TYPE_HINT,
        })

        rules_checker._check_functions_have_type_hint()

        self.assertEqual(
            sorted(rules_checker._recommendations[FUNCTION_TYPE_HINT]),
            sorted([str(func) for func in FUNCTIONS_WITHOUT_TYPE_HINT]),
        )


@tag('refactoring_services', 'refactoring_services_rules_checker')
class DocstringCheckerMixinTests(TestCase):
    """Test DocstringCheckerMixin mixin"""

    def test_check_functions_and_classes_have_docstring(self) -> None:
        """Test _check_functions_and_classes_have_docstring method"""

        rules_checker = CleanCodeRulesChecker({
            'functions':
                FUNCTIONS_WITH_DOCSTRING + FUNCTIONS_WITHOUT_DOCSTRING,
            'classes':
                CLASSES_WITH_DOCSTRING + CLASSES_WITHOUT_DOCSTRING,
        })

        rules_checker._check_functions_and_classes_have_docstring()

        self.assertEqual(
            sorted(rules_checker._recommendations[FUNCTION_DOCSTRING]),
            sorted([str(func) for func in FUNCTIONS_WITHOUT_DOCSTRING]),
        )

        self.assertEqual(
            sorted(rules_checker._recommendations[CLASS_DOCSTRING]),
            sorted([str(class_) for class_ in CLASSES_WITHOUT_DOCSTRING]),
        )


@tag('refactoring_services', 'refactoring_services_rules_checker')
class NamingStyleCheckerMixinTests(TestCase):
    """Test NamingStyleCheckerMixin mixin"""

    def test_check_functions_naming_style_is_snake_case(self) -> None:
        """Test _check_functions_naming_style_is_snake_case method"""

        rules_checker = CleanCodeRulesChecker({
            'functions':
                CORRECT_SNAKE_CASE_FUNCTIONS + INCORRECT_SNAKE_CASE_FUNCTIONS,
        })

        rules_checker._check_functions_naming_style_is_snake_case()

        self.assertEqual(
            sorted(rules_checker._recommendations[SNAKE_CASE_STYLE]),
            sorted([str(func) for func in INCORRECT_SNAKE_CASE_FUNCTIONS]),
        )

    def test_check_classes_naming_style_is_cap_words(self) -> None:
        """Test _check_classes_naming_style_is_cap_words method"""

        rules_checker = CleanCodeRulesChecker({
            'classes':
                CORRECT_CAP_WORDS_CLASSES + INCORRECT_CAP_WORDS_CLASSES,
        })

        rules_checker._check_classes_naming_style_is_cap_words()

        self.assertEqual(
            sorted(rules_checker._recommendations[CAP_WORDS_STYLE]),
            sorted([str(func) for func in INCORRECT_CAP_WORDS_CLASSES]),
        )


@tag('refactoring_services', 'refactoring_services_rules_checker')
class NamingCheckerMixinTests(TestCase):
    """Test NamingCheckerMixin mixin"""

    def test_check_not_bool_functions_start_with_get(self) -> None:
        """Test _check_not_bool_functions_start_with_get method"""

        rules_checker = CleanCodeRulesChecker({
            'functions': CORRECT_GET_FUNCTIONS + INCORRECT_GET_FUNCTIONS,
        })

        rules_checker._check_not_bool_functions_start_with_get()

        self.assertEqual(
            sorted(rules_checker._recommendations[PREFIX_GET]),
            sorted([str(func) for func in INCORRECT_GET_FUNCTIONS]),
        )

    def test_check_bool_functions_start_with_is(self) -> None:
        """Test _check_bool_functions_start_with_is method"""

        rules_checker = CleanCodeRulesChecker({
            'functions': CORRECT_BOOL_FUNCTIONS + INCORRECT_BOOL_FUNCTIONS,
        })

        rules_checker._check_bool_functions_start_with_is()

        self.assertEqual(
            sorted(rules_checker._recommendations[PREFIX_IS]),
            sorted([str(func) for func in INCORRECT_BOOL_FUNCTIONS]),
        )
