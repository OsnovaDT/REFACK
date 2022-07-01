"""Refactoring recommendations generator.

Check user's code on clean code rules and generate recommendations.

Clean code rules:
1. From PEP8:
    1) All functions and methods have snake_case naming style;
    2) All classes have CamelCase naming style;
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
    PREFIX_GET, PREFIX_IS, SNAKE_CASE_STYLE, CAMEL_CASE_STYLE,
    FUNCTION_DOCUMENTATION, CLASS_DOCUMENTATION, FUNCTION_TYPE_HINT,
    ARGUMENT_TYPE_HINT, BOOL_TYPE, NOT_BOOL_TYPE, NamingStyle,
)


def is_bool_function_correct(name: str, type_: str) -> bool:
    """Check function that returned a boolean

    Return True if the function starts with «is» prefix"""

    match name, type_:
        case str(name), str(type_):
            is_function_correct = type_ == BOOL_TYPE \
                and name.startswith('is') \
                and name != 'is' \
                and name != 'is_'
        case _:
            is_function_correct = False

    return bool(is_function_correct)


def is_get_function_correct(name: str, type_: str) -> bool:
    """Check function that returned a value (exclude bool)

    Return True if the function starts with «get» prefix"""

    match name, type_:
        case str(name), str(type_):
            is_function_correct = type_ == NOT_BOOL_TYPE \
                and name.startswith('get') \
                and name != 'get' \
                and name != 'get_'
        case _:
            is_function_correct = False

    return bool(is_function_correct)


class RecommendationsGenerator:
    """Check code on clean code rules and generate recommendations"""

    def __init__(self, code_modules: dict):
        self.code_modules = code_modules
        self.__recommendations = defaultdict(list)

    def generate(self) -> None:
        """Check code for all the rules and generate recommendations"""

        self.__get_functions_starts_with_get()
        self.__bool_functions_starts_with_is()
        self.__functions_naming_style_is_snake_case()
        self.__classes_naming_style_is_camel_case()
        self.__all_modules_have_documentation()
        self.__all_functions_have_type_hint()
        self.__all_functions_have_type_hint_for_arguments()

    @property
    def __functions(self) -> tuple:
        """Return functions from the code"""

        if 'functions' in self.code_modules.keys():
            code_functions = self.code_modules['functions']
        else:
            code_functions = []

        return tuple(code_functions)

    @property
    def __classes(self) -> tuple:
        """Return classes from the code"""

        if 'classes' in self.code_modules.keys():
            code_classes = self.code_modules['classes']
        else:
            code_classes = []

        return tuple(code_classes)

    def __get_naming_style(self, name: str) -> NamingStyle:
        """Return naming style for the name.

        Possible naming styles:
        1) Snake case - get_user_login
        2) Camel case - getUserLogin or GetUserLogin

        """

        naming_style = ''

        if name.islower() and '_' in name:
            naming_style = NamingStyle.SNAKE_CASE
        else:
            naming_style = NamingStyle.CAMEL_CASE

        return naming_style

    def __all_modules_have_documentation(self) -> None:
        """Check that all modules have documentation"""

        for func in self.__functions:
            if not func.docstring:
                self.__recommendations[
                    FUNCTION_DOCUMENTATION
                ].append(func.name)

        for class_ in self.__classes:
            if not class_.docstring:
                self.__recommendations[
                    CLASS_DOCUMENTATION
                ].append(class_.name)

    def __all_functions_have_type_hint_for_arguments(self) -> None:
        """Check that all functions have type annotation for arguments"""

        for func in self.__functions:
            for arg in func.args:
                if not arg.annotation:
                    self.__recommendations[
                        ARGUMENT_TYPE_HINT
                    ].append(f'аргумент "{arg.arg}" для функции {func.name}')

    def __all_functions_have_type_hint(self) -> None:
        """Check that all functions have type annotation (e.g. -> str)"""

        for func in self.__functions:
            if not func.type_hint:
                self.__recommendations[
                    FUNCTION_TYPE_HINT
                ].append(func.name)

    def __functions_naming_style_is_snake_case(self) -> None:
        """Check that functions and methods have Snake case naming style"""

        for func in self.__functions:
            naming_style = self.__get_naming_style(func.name)

            if naming_style != NamingStyle.SNAKE_CASE:
                self.__recommendations[SNAKE_CASE_STYLE].append(func.name)

    def __classes_naming_style_is_camel_case(self) -> None:
        """Check that classes have Camel case naming style"""

        for class_ in self.__classes:
            naming_style = self.__get_naming_style(class_.name)

            if naming_style != NamingStyle.CAMEL_CASE:
                self.__recommendations[CAMEL_CASE_STYLE].append(class_.name)

    def __get_functions_starts_with_get(self) -> None:
        """Check that return functions start with the «get» prefix

        Example:
        1) get_value - not error
        2) server_handling - error
        3) getUserId - not error
        4) calculatePrise - error

        """

        for func in self.__functions:
            if func.type == NOT_BOOL_TYPE and \
                    not is_get_function_correct(func.name, func.type):
                self.__recommendations[PREFIX_GET].append(func.name)

    def __bool_functions_starts_with_is(self) -> None:
        """Check that bool return functions start with the «is» prefix

        Example:
        1) is_empty - not error
        2) check_empty - error
        3) isValid - not error
        4) valid - error

        """

        for func in self.__functions:
            if func.type == BOOL_TYPE \
                    and not is_bool_function_correct(func.name, func.type):
                self.__recommendations[PREFIX_IS].append(func.name)

    @property
    def recommendations(self) -> dict:
        """Refactoring recommendations"""

        return self.__recommendations
