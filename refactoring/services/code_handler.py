"""Handle user's code.

1. Parse the code;
2. Generate refactoring recommendations.

"""

from ast import parse

from refactoring.services.code_parser import CodeParser
from refactoring.services.rules_checker import CleanCodeRulesChecker


class CodeHandler:
    """Contain user's code recommendations"""

    def __init__(self, code: str):
        parser = CodeParser()
        parser.visit(parse(code))

        self.__rules_checker = CleanCodeRulesChecker(
            parser.code_items
        )

    @property
    def recommendations(self) -> dict:
        """Recommendations for refactoring user's code"""

        return self.__rules_checker.recommendations