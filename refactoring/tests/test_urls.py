"""Tests urls of refactoring app"""

from django.test import tag

from config.constants.tests import RULES, INDEX, CODE_INPUT
from config.tests.mixins import (
    Test200IfAuthorizedMixin, Test302IfNotAuthorizedMixin,
)


@tag('refactoring_urls')
class PagesTests(Test302IfNotAuthorizedMixin, Test200IfAuthorizedMixin):
    """Test pages of refactoring app"""

    def test_index(self) -> None:
        """Test index page"""

        self._test_302_if_not_authorized(INDEX)
        self._test_200_if_authorized(INDEX)

    def test_code_input(self) -> None:
        """Test code input page"""

        self._test_302_if_not_authorized(CODE_INPUT)
        self._test_200_if_authorized(CODE_INPUT)

    def test_rules(self) -> None:
        """Test rules page"""

        self._test_302_if_not_authorized(RULES)
        self._test_200_if_authorized(RULES)
