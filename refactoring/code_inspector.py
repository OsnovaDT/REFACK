"""Class that inspect the code and save it's errors"""

from ast import parse
from collections import defaultdict

from refactoring.code_parser import CodeParser
from refactoring.constants import ERROR_PREFIX_GET, ERROR_PREFIX_IS


def is_bool_function_correct(name: str, type_: str) -> bool:
    """Check function that returned a boolean

    Return True if the function starts with «is» prefix"""

    match name, type_:
        case str(name), str(type_):
            is_function_correct = type_ == 'return bool' \
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
            is_function_correct = type_ == 'return' \
                and name.startswith('get') \
                and name != 'get' \
                and name != 'get_'
        case _:
            is_function_correct = False

    return bool(is_function_correct)


class CodeInspector:
    """Parse the code, check it on rules and save errors"""

    def __init__(self, code: str):
        code_parser = CodeParser()
        code_parser.visit(parse(code))

        self.code_rule_checker = CodeRuleChecker(code_parser.modules)
        self.code_rule_checker._check_all_rules()

    @property
    def errors(self) -> dict:
        """Code errors received from code checker"""

        return dict(self.code_rule_checker.errors)


class CodeRuleChecker:
    """Contains methods for checking code on the rules"""

    def __init__(self, code_modules: dict):
        self.code_modules = code_modules
        self.errors = defaultdict(list)

    def _check_all_rules(self) -> None:
        """Check code for all the rules"""

        self.__get_functions_starts_with_get()
        self.__bool_functions_starts_with_is()

    @property
    def __functions(self) -> tuple:
        """Return functions from the code"""

        if 'functions' in self.code_modules.keys():
            code_functions = self.code_modules['functions']
        else:
            code_functions = []

        return tuple(code_functions)

    def __get_functions_starts_with_get(self) -> None:
        """Check that return functions start with the «get» prefix

        Example:
        1) get_value - not error
        2) server_handling - error
        3) getUserId - not error
        4) calculatePrise - error

        """

        for name, type_ in self.__functions:
            if type_ == 'return' and not is_get_function_correct(name, type_):
                self.errors[ERROR_PREFIX_GET].append(name)

    def __bool_functions_starts_with_is(self) -> None:
        """Check that bool return functions start with the «is» prefix

        Example:
        1) is_empty - not error
        2) check_empty - error
        3) isValid - not error
        4) valid - error

        """

        for name, type_ in self.__functions:
            if type_ == 'return bool' \
                    and not is_bool_function_correct(name, type_):
                self.errors[ERROR_PREFIX_IS].append(name)
