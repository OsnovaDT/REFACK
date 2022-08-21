"""Test services.files_download module"""

from json import loads

from django.test import TestCase, tag
from django.http import JsonResponse

from refactoring.services.files_download import _get_json_file_response
from refactoring.tests.constants import FILE_CONTENT


@tag('refactoring_services', 'refactoring_services_files_download')
class FilesDownloadTests(TestCase):
    """Test functions from files_download module"""

    def test_get_json_file_response(self) -> None:
        """Test _get_json_file_response function"""

        real_response = _get_json_file_response(FILE_CONTENT).__dict__

        expected_response = JsonResponse(
            loads(FILE_CONTENT), json_dumps_params={'ensure_ascii': False},
        ).__dict__

        self.assertEqual(
            real_response['_container'], expected_response['_container'],
        )

        self.assertEqual(
            real_response['headers'], expected_response['headers'],
        )
