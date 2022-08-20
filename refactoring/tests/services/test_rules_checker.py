"""Test services.rules_checker module"""

from django.test import TestCase, tag

from refactoring.services.rules_checker import CleanCodeRulesChecker
from refactoring.tests.constants import (
    ARGUMENT_TYPE_HINT, CLASSES_WITHOUT_DOCSTRING, CLASS_DOCSTRING,
    CLASSES_WITH_DOCSTRING, FUNCTIONS_WITH_ARGS, FUNCTION_TYPE_HINT,
    FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT_ERRORS, FUNCTIONS_WITH_TYPE_HINT,
    FUNCTIONS_WITHOUT_TYPE_HINT, FUNCTIONS_WITH_DOCSTRING, FUNCTION_DOCSTRING,
    FUNCTIONS_WITHOUT_DOCSTRING,
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
