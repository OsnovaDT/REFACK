"""Refactoring recommendations generator.

Check user's code on clean code rules
and generate refactoring recommendations.

"""

from collections import defaultdict

from refactoring.services.rules_checkers import CleanCodeRulesChecker


class RecommendationsGenerator(CleanCodeRulesChecker):
    """Generate and return refactoring recommendations"""

    def __init__(self, code_items: dict):
        self._code_items = code_items
        self._recommendations = defaultdict(list)

    @property
    def recommendations(self) -> dict:
        """Recommendations for refactoring user code"""

        self.check_all_rules()

        return self._recommendations
