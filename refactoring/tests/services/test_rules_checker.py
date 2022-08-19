"""Test services.rules_checker module"""

from django.test import TestCase, tag

from refactoring.services.rules_checker import CleanCodeRulesChecker
from refactoring.tests.constants import (
    ARGUMENT_TYPE_HINT, FUNCTIONS_WITH_ARG_TYPE_HINT,
    FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT_ERRORS,
)


@tag('refactoring_services', 'refactoring_services_rules_checker')
class TypeHintCheckerMixinTests(TestCase):
    """Test TypeHintCheckerMixin mixin"""

    def test_check_functions_args_have_type_hints(self) -> None:
        """Test _check_functions_args_have_type_hints method"""

        rules_checker = CleanCodeRulesChecker({
            'functions': FUNCTIONS_WITH_ARG_TYPE_HINT,
        })

        rules_checker._check_functions_args_have_type_hints()

        self.assertEqual(
            sorted(rules_checker._recommendations[ARGUMENT_TYPE_HINT]),
            FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT_ERRORS,
        )
