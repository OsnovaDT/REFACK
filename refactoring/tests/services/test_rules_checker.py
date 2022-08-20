"""Test services.rules_checker module"""

from django.test import TestCase, tag

from refactoring.services.rules_checker import (
    CleanCodeRulesChecker, NamingStyleCheckerMixin, NamingCheckerMixin,
    TypeHintCheckerMixin, DocstringCheckerMixin,
)
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
    PREFIX_GET, PREFIX_IS, BOOL_TYPE, ALL_RULES_FUNCTIONS, ALL_RULES_CLASSES,
    get_arg_type_hint_error,
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

    def test_mro(self) -> None:
        """Test that NamingStyleCheckerMixin in NamingCheckerMixin MRO"""

        self.assertIn(NamingStyleCheckerMixin, NamingCheckerMixin.mro())


@tag('refactoring_services', 'refactoring_services_rules_checker')
class CleanCodeRulesCheckerTests(TestCase):
    """Test CleanCodeRulesChecker mixin"""

    def setUp(self) -> None:
        self.all_functions = CORRECT_BOOL_FUNCTIONS + CORRECT_GET_FUNCTIONS + \
            INCORRECT_BOOL_FUNCTIONS + INCORRECT_GET_FUNCTIONS

        self.all_classes = CORRECT_CAP_WORDS_CLASSES + \
            INCORRECT_CAP_WORDS_CLASSES

        self.rules_checker_without_code_items = CleanCodeRulesChecker({})

        self.rules_checker = CleanCodeRulesChecker({
            'functions': self.all_functions,
            'classes': self.all_classes,
        })

    def test_mro(self) -> None:
        """Test that clean code mixins in CleanCodeRulesChecker MRO"""

        clean_code_mixins = (
            TypeHintCheckerMixin, DocstringCheckerMixin, NamingCheckerMixin,
        )

        for mixin in clean_code_mixins:
            self.assertIn(mixin, CleanCodeRulesChecker.mro())

    def test_functions_property(self) -> None:
        """Test _functions property"""

        self.assertEqual(
            self.rules_checker_without_code_items._functions,
            set(),
        )

        self.assertEqual(
            self.rules_checker._functions,
            set(reversed(self.all_functions)),
        )

    def test_classes_property(self) -> None:
        """Test _classes property"""

        self.assertEqual(
            self.rules_checker_without_code_items._classes,
            set(),
        )

        self.assertEqual(
            self.rules_checker._classes,
            set(reversed(self.all_classes)),
        )

    def test_not_bool_functions_property(self) -> None:
        """Test _not_bool_functions property"""

        self.assertEqual(
            self.rules_checker_without_code_items._not_bool_functions,
            set(),
        )

        self.assertEqual(
            self.rules_checker._not_bool_functions,
            {
                func for func in set(reversed(self.all_functions))
                if func.type != BOOL_TYPE
            },
        )

    def test_bool_functions_property(self) -> None:
        """Test _bool_functions property"""

        self.assertEqual(
            self.rules_checker_without_code_items._bool_functions,
            set(),
        )

        self.assertEqual(
            self.rules_checker._bool_functions,
            {
                func for func in set(reversed(self.all_functions))
                if func.type == BOOL_TYPE
            },
        )

    def test_recommendations_property(self) -> None:
        """Test recommendations property"""

        rules_checker = CleanCodeRulesChecker({
            'functions': ALL_RULES_FUNCTIONS,
            'classes': ALL_RULES_CLASSES,
        })

        self.assertEqual(
            {
                rule: sorted(code_items)
                for rule, code_items
                in dict(rules_checker.recommendations).items()
            },
            {
                # Naming
                PREFIX_GET: [str(ALL_RULES_FUNCTIONS[1])],

                PREFIX_IS: [str(ALL_RULES_FUNCTIONS[3])],

                # Naming style
                SNAKE_CASE_STYLE: sorted([
                    str(ALL_RULES_FUNCTIONS[1]),
                    str(ALL_RULES_FUNCTIONS[3]),
                ]),

                CAP_WORDS_STYLE: sorted([
                    str(ALL_RULES_CLASSES[0]),
                    str(ALL_RULES_CLASSES[1]),
                    str(ALL_RULES_CLASSES[2]),
                ]),

                # Docstring

                FUNCTION_DOCSTRING: sorted([
                    str(ALL_RULES_FUNCTIONS[1]),
                    str(ALL_RULES_FUNCTIONS[3]),
                ]),

                CLASS_DOCSTRING: sorted([
                    str(ALL_RULES_CLASSES[1]),
                    str(ALL_RULES_CLASSES[2])
                ]),

                # Type hint

                FUNCTION_TYPE_HINT: sorted([
                    str(ALL_RULES_FUNCTIONS[1]),
                    str(ALL_RULES_FUNCTIONS[3]),
                ]),

                ARGUMENT_TYPE_HINT: sorted([
                    get_arg_type_hint_error(
                        "value2", str(ALL_RULES_FUNCTIONS[1]),
                    ),
                    get_arg_type_hint_error(
                        "value1", str(ALL_RULES_FUNCTIONS[2]),
                    ),
                    get_arg_type_hint_error(
                        "value2", str(ALL_RULES_FUNCTIONS[2]),
                    ),
                ]),
            }
        )

    def test_check_all_rules(self) -> None:
        """Test __check_all_rules method"""

        rules_checker = CleanCodeRulesChecker({
            'functions': ALL_RULES_FUNCTIONS,
            'classes': ALL_RULES_CLASSES,
        })

        rules_checker._CleanCodeRulesChecker__check_all_rules()

        # Check _check_not_bool_functions_start_with_get
        self.assertEqual(
            rules_checker._recommendations[PREFIX_GET],
            [str(ALL_RULES_FUNCTIONS[1])],
        )

        # Check _check_bool_functions_start_with_is
        self.assertEqual(
            rules_checker._recommendations[PREFIX_IS],
            [str(ALL_RULES_FUNCTIONS[3])],
        )

        # Check _check_functions_naming_style_is_snake_case
        self.assertEqual(
            sorted(rules_checker._recommendations[SNAKE_CASE_STYLE]),
            sorted([str(ALL_RULES_FUNCTIONS[1]), str(ALL_RULES_FUNCTIONS[3])]),
        )

        # Check _check_classes_naming_style_is_cap_words
        self.assertEqual(
            sorted(rules_checker._recommendations[CAP_WORDS_STYLE]),
            sorted([
                str(ALL_RULES_CLASSES[0]),
                str(ALL_RULES_CLASSES[1]),
                str(ALL_RULES_CLASSES[2]),
            ]),
        )

        # Check _check_functions_and_classes_have_docstring
        self.assertEqual(
            sorted(rules_checker._recommendations[FUNCTION_DOCSTRING]),
            sorted([str(ALL_RULES_FUNCTIONS[1]), str(ALL_RULES_FUNCTIONS[3])]),
        )

        self.assertEqual(
            sorted(rules_checker._recommendations[CLASS_DOCSTRING]),
            sorted([str(ALL_RULES_CLASSES[1]), str(ALL_RULES_CLASSES[2])]),
        )

        # Check _check_functions_have_type_hint
        self.assertEqual(
            sorted(rules_checker._recommendations[FUNCTION_TYPE_HINT]),
            sorted([str(ALL_RULES_FUNCTIONS[1]), str(ALL_RULES_FUNCTIONS[3])]),
        )

        # Check _check_functions_args_have_type_hints
        self.assertEqual(
            sorted(rules_checker._recommendations[ARGUMENT_TYPE_HINT]),
            sorted([
                get_arg_type_hint_error("value2", str(ALL_RULES_FUNCTIONS[1])),
                get_arg_type_hint_error("value1", str(ALL_RULES_FUNCTIONS[2])),
                get_arg_type_hint_error("value2", str(ALL_RULES_FUNCTIONS[2])),
            ]),
        )
