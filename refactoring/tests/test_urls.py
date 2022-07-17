"""Tests urls of refactoring app"""

from unittest import expectedFailure

from django.test import tag

from config.tests.constants import (
    RULES, INDEX, CODE_INPUT, SAVED_RECOMMENDATIONS, CODE_REFACTORING,
    DOWNLOAD_JSON, DOWNLOAD_PDF, DOWNLOAD_XML, SAVE_RECOMMENDATION,
)
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

    def test_saved_recommendations(self) -> None:
        """Test saved_recommendations page"""

        self._test_302_if_not_authorized(SAVED_RECOMMENDATIONS)
        self._test_200_if_authorized(SAVED_RECOMMENDATIONS)

    def test_rules(self) -> None:
        """Test rules page"""

        self._test_302_if_not_authorized(RULES)
        self._test_200_if_authorized(RULES)

    def test_code_refactoring(self) -> None:
        """Test code_refactoring page"""

        self._test_302_if_not_authorized(CODE_REFACTORING)
        self._test_200_if_authorized(CODE_REFACTORING)

    @expectedFailure
    def test_download_pages(self) -> None:
        """Test pages for downloading recommendations files"""

        post_data = {'results': 'def test_func(): return 1'}

        for path in (DOWNLOAD_JSON, DOWNLOAD_PDF, DOWNLOAD_XML):
            self._test_302_if_not_authorized(path, post_data)
            self._test_200_if_authorized(path, post_data)

    def test_save_recommendation(self) -> None:
        """Test save_recommendation page"""

        self._test_302_if_not_authorized(SAVE_RECOMMENDATION)
        self._test_200_if_authorized(SAVE_RECOMMENDATION)
