"""Handle user's code.

1. Parse the code;
2. Generate refactoring recommendations.

"""

from ast import parse

from refactoring.services.code_parser import CodeParser
from refactoring.services.recommendations_generator import (
    RecommendationsGenerator,
)


class CodeHandler:
    """Contain user's code recommendations"""

    def __init__(self, code: str):
        parser = CodeParser()
        parser.visit(parse(code))

        self.__recommendations_generator = RecommendationsGenerator(
            parser.code_items
        )

    @property
    def recommendations(self) -> dict:
        """Recommendations for refactoring user's code"""

        self.__recommendations_generator.generate()

        return self.__recommendations_generator.recommendations
