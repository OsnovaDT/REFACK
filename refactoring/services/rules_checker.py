"""Contain class that check user's code on clean code rules
and generate refactoring recommendations.

Clean code rules:
1. From PEP 8:
    1) All functions and methods have snake_case naming style;
    2) All classes have CapWords naming style;
    3) All functions, methods and classes have documentation.

2. Others:
    1) If function / method returns boolean, its name should starts
        with «is» prefix;
    2) If function / method returns not boolean, its name should starts
        with «get» prefix;
    3) All functions and methods have type hints;
    4) All arguments for functions / methods have type hints.

"""

from collections import defaultdict

from refactoring.services.constants import (
    PREFIX_GET, PREFIX_IS, SNAKE_CASE_STYLE, CAP_WORDS_STYLE,
    FUNCTION_DOCSTRING, CLASS_DOCSTRING, FUNCTION_TYPE_HINT,
    ARGUMENT_TYPE_HINT, BOOL_TYPE,
)
from refactoring.services.utils import (
    is_in_cap_words, is_in_snake_case, get_code_items_without_duplicates,
)


class TypeHintCheckerMixin:
    """Check type hints for functions and their arguments.

    About type hints you can read here:
    https://peps.python.org/pep-0484/

    """

    def _check_functions_args_have_type_hints(self) -> None:
        """Check type hints for functions arguments"""

        for func in self._functions:
            for arg in func.args:
                if not arg.annotation:
                    self._recommendations[ARGUMENT_TYPE_HINT].append(
                        f'аргумент «{arg.arg}» (функция «{func.name}»)'
                    )

    def _check_functions_have_type_hint(self) -> None:
        """Check type hints for functions"""

        for func in self._functions:
            if not func.type_hint:
                self._recommendations[FUNCTION_TYPE_HINT].append(func.name)


class DocstringCheckerMixin:
    """Check that functions and classes have docstrings.

    About docstrings you can read here:
    https://peps.python.org/pep-0008/#documentation-strings

    """

    def _check_functions_and_classes_have_docstring(self) -> None:
        """Check that functions and classes have docstring"""

        for func in self._functions:
            if not func.docstring:
                self._recommendations[FUNCTION_DOCSTRING].append(func.name)

        for class_ in self._classes:
            if not class_.docstring:
                self._recommendations[CLASS_DOCSTRING].append(class_.name)


class NamingStyleCheckerMixin:
    """Check naming style for functions and classes"""

    def _check_functions_naming_style_is_snake_case(self) -> None:
        """Check that naming style for functions is snake_case.

        About this rule you can read here:
        https://peps.python.org/pep-0008/#function-and-variable-names

        """

        for func in self._functions:
            if not is_in_snake_case(func.name):
                self._recommendations[SNAKE_CASE_STYLE].append(func.name)

    def _check_classes_naming_style_is_cap_words(self) -> None:
        """Check that naming style for classes is CapWords.

        About this rule you can read here:
        https://peps.python.org/pep-0008/#class-names

        """

        for class_ in self._classes:
            if not is_in_cap_words(class_.name):
                self._recommendations[CAP_WORDS_STYLE].append(class_.name)


class NamingCheckerMixin(NamingStyleCheckerMixin):
    """Check naming for functions"""

    def _check_not_bool_functions_start_with_get(self) -> None:
        """Check that not bool functions start with «get» prefix.

        Examples:
        1. get_value - correct;
        2. server_handling - not correct;
        3. getUserId - not correct;
        4. calculatePrise - not correct.

        """

        for func in self._not_bool_functions:
            if not func.is_start_with_prefix_get_():
                self._recommendations[PREFIX_GET].append(func.name)

    def _check_bool_functions_start_with_is(self) -> None:
        """Check that bool functions start with «is» prefix.

        Examples:
        1. is_empty - correct;
        2. check_empty - not correct;
        3. isValid - not correct;
        4. valid - not correct.

        """

        for func in self._bool_functions:
            if not func.is_start_with_prefix_is_():
                self._recommendations[PREFIX_IS].append(func.name)


class CleanCodeRulesChecker(
        TypeHintCheckerMixin, DocstringCheckerMixin, NamingCheckerMixin):
    """Check code on clean code rules and generate recommendations"""

    def __init__(self, code_items: dict):
        self.__code_items = code_items
        self._recommendations = defaultdict(list)

    @property
    def recommendations(self) -> dict:
        """Recommendations for refactoring user's code"""

        self.__check_all_rules()

        return self._recommendations

    @property
    def _functions(self) -> set:
        """Return functions from the code"""

        code_functions = self.__code_items.get('functions', [])

        return get_code_items_without_duplicates(code_functions)

    @property
    def _classes(self) -> set:
        """Return classes from the code"""

        code_classes = self.__code_items.get('classes', [])

        return get_code_items_without_duplicates(code_classes)

    @property
    def _not_bool_functions(self) -> set:
        """Return not boolean functions from the code"""

        return self._functions - self._bool_functions

    @property
    def _bool_functions(self) -> set:
        """Return boolean functions from the code"""

        return {func for func in self._functions if func.type == BOOL_TYPE}

    def __check_all_rules(self) -> None:
        """Check code on all clean code rules"""

        # Naming
        self._check_not_bool_functions_start_with_get()
        self._check_bool_functions_start_with_is()

        # Naming style
        self._check_functions_naming_style_is_snake_case()
        self._check_classes_naming_style_is_cap_words()

        # Docstring
        self._check_functions_and_classes_have_docstring()

        # Type hint
        self._check_functions_have_type_hint()
        self._check_functions_args_have_type_hints()
