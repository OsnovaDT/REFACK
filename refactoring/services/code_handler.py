"""Class that inspect the code and save it's errors"""

from ast import parse

from refactoring.services.code_parser import CodeParser
from refactoring.services.rules_checker import CodeRulesChecker


class CodeHandler:
    """Parse the code, check it on rules and save errors"""

    def __init__(self, code: str):
        code_parser = CodeParser()
        code_parser.visit(parse(code))

        self.__code_rules_checker = CodeRulesChecker(code_parser.modules)
        self.__code_rules_checker._check_all_rules()

    @property
    def recommendations(self) -> dict:
        """Code recommendations received from code checker"""

        return dict(self.__code_rules_checker.errors)
