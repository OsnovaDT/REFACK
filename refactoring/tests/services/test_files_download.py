"""Test services.files_download module"""

from json import loads

from django.test import TestCase, tag
from django.http import JsonResponse, FileResponse

from refactoring.services.files_download import (
    _get_json_response, _add_file_disposition_to_response,
)
from refactoring.tests.constants import (
    FILE_CONTENT, EXTENSTION_AND_RESPONSE, NOT_STRING_VALUES,
)


@tag('refactoring_services', 'refactoring_services_files_download')
class FilesDownloadTests(TestCase):
    """Test functions from files_download module"""

    def test_get_json_response(self) -> None:
        """Test _get_json_response function"""

        real_response = _get_json_response(FILE_CONTENT).__dict__

        expected_response = JsonResponse(
            loads(FILE_CONTENT), json_dumps_params={'ensure_ascii': False},
        ).__dict__

        self.assertEqual(
            real_response['_container'], expected_response['_container'],
        )

        self.assertEqual(
            real_response['headers'], expected_response['headers'],
        )

        for value in NOT_STRING_VALUES:
            self.assertEqual(
                _get_json_response(value).__dict__, JsonResponse({}).__dict__,
            )

    def test_add_file_disposition_to_response(self) -> None:
        """Test _add_file_disposition_to_response function"""

        for extenstion, response in EXTENSTION_AND_RESPONSE.items():
            _add_file_disposition_to_response(response, f'test.{extenstion}')

            self.assertEqual(
                response['Content-Disposition'],
                f'attachment; filename=test.{extenstion};',
            )

        for value in NOT_STRING_VALUES:
            file_response = FileResponse()

            _add_file_disposition_to_response(file_response, value)

            self.assertEqual(
                file_response['Content-Disposition'],
                'attachment; filename=;',
            )

        for value in NOT_STRING_VALUES:
            _add_file_disposition_to_response(value, 'test.pdf')
