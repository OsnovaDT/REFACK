"""Tests urls of refactoring app"""

from django.test import tag

from config.tests.constants import (
    RULES, INDEX, CODE_INPUT, SAVED_RECOMMENDATIONS, CODE_REFACTORING,
    DOWNLOAD_JSON, DOWNLOAD_PDF, DOWNLOAD_XML, SAVE_RECOMMENDATION,
)
from config.tests.mixins import TestURLMixin
from refactoring.tests.constants import TEST_REFACTORING_RESULTS


@tag('refactoring_urls')
class PagesTests(TestURLMixin):
    """Test pages of refactoring app"""

    def test_index(self) -> None:
        """Test index page"""

        self._test_url(INDEX)
        self._test_url(INDEX, 200, True)

    def test_code_input(self) -> None:
        """Test code input page"""

        self._test_url(CODE_INPUT)
        self._test_url(CODE_INPUT, 200, True)

    def test_saved_recommendations(self) -> None:
        """Test saved_recommendations page"""

        self._test_url(SAVED_RECOMMENDATIONS)
        self._test_url(SAVED_RECOMMENDATIONS, 200, True)

    def test_rules(self) -> None:
        """Test rules page"""

        self._test_url(RULES)
        self._test_url(RULES, 200, True)

    def test_code_refactoring(self) -> None:
        """Test code_refactoring page"""

        self._test_url(CODE_REFACTORING)
        self._test_url(CODE_REFACTORING, 200, True)

    def test_download_json(self) -> None:
        """Test download_json page"""

        self._test_url(DOWNLOAD_JSON, data=TEST_REFACTORING_RESULTS)
        self._test_url(DOWNLOAD_JSON, 200, True, TEST_REFACTORING_RESULTS)

    def test_download_pdf(self) -> None:
        """Test download_pdf page"""

        self._test_url(DOWNLOAD_PDF, data=TEST_REFACTORING_RESULTS)
        self._test_url(DOWNLOAD_PDF, 200, True, TEST_REFACTORING_RESULTS)

    def test_download_xml(self) -> None:
        """Test download_xml page"""

        self._test_url(DOWNLOAD_XML, data=TEST_REFACTORING_RESULTS)
        self._test_url(DOWNLOAD_XML, 200, True, TEST_REFACTORING_RESULTS)

    def test_save_recommendation(self) -> None:
        """Test save_recommendation page"""

        self._test_url(SAVE_RECOMMENDATION)
        self._test_url(SAVE_RECOMMENDATION, 200, True)
