"""Tests for services.files_download module"""

from json import loads

from dicttoxml import dicttoxml
from django.http import FileResponse, JsonResponse
from django.test import tag, TestCase

from refactoring.services.files_download import (
    get_response_with_file,
    get_xml_file_content,
    _get_json_response,
    _add_file_disposition_to_response,
)
from refactoring.tests.constants import (
    EXTENSION_AND_RESPONSE,
    FILE_CONTENT,
    NOT_STRING_VALUES,
)


@tag("refactoring_services", "refactoring_services_files_download")
class FilesDownloadTests(TestCase):
    """Test functions from files_download module"""

    def test_get_json_response(self) -> None:
        """Test _get_json_response function"""

        real_response = _get_json_response(FILE_CONTENT).__dict__

        expected_response = JsonResponse(
            loads(FILE_CONTENT),
            json_dumps_params={"ensure_ascii": False},
        ).__dict__

        self.assertEqual(
            real_response["_container"],
            expected_response["_container"],
        )

        self.assertEqual(
            real_response["headers"],
            expected_response["headers"],
        )

        for value in NOT_STRING_VALUES:
            self.assertEqual(
                _get_json_response(value).__dict__,
                JsonResponse({}).__dict__,
            )

    def test_add_file_disposition_to_response(self) -> None:
        """Test _add_file_disposition_to_response function"""

        for extension, response in EXTENSION_AND_RESPONSE.items():
            _add_file_disposition_to_response(response, f"test.{extension}")

            self.assertEqual(
                response["Content-Disposition"],
                f"attachment; filename=test.{extension};",
            )

        for value in NOT_STRING_VALUES:
            file_response = FileResponse()

            _add_file_disposition_to_response(file_response, value)

            self.assertEqual(
                file_response["Content-Disposition"],
                "attachment; filename=;",
            )

        for value in NOT_STRING_VALUES:
            _add_file_disposition_to_response(value, "test.pdf")

    def test_get_xml_file_content(self) -> None:
        """Test get_xml_file_content function"""

        self.assertEqual(
            get_xml_file_content(FILE_CONTENT),
            str(dicttoxml(loads(FILE_CONTENT))),
        )

        for value in NOT_STRING_VALUES:
            self.assertEqual(get_xml_file_content(value), "")

    def test_get_response_with_file(self) -> None:
        """Test get_response_with_file function"""

        # PDF and XML

        test_name = "test"

        for extension in ("pdf", "xml"):
            file_response = get_response_with_file(
                FILE_CONTENT, f"{test_name}.{extension}"
            )

            self.assertTrue(isinstance(file_response, FileResponse))

            # Headers

            self.assertEqual(
                file_response["Content-Type"],
                f"application/{extension}",
            )

            self.assertEqual(
                file_response["Content-Disposition"],
                f"attachment; filename={test_name}.{extension};",
            )

        # JSON

        real_json_response = get_response_with_file(
            FILE_CONTENT,
            f"{test_name}.json",
        )

        expected_json_response = JsonResponse(
            loads(FILE_CONTENT),
            json_dumps_params={"ensure_ascii": False},
        )

        self.assertTrue(isinstance(real_json_response, JsonResponse))

        self.assertEqual(
            real_json_response.__dict__["_container"],
            expected_json_response.__dict__["_container"],
        )

        # Headers

        self.assertEqual(
            real_json_response["Content-Type"], "application/json"
        )

        self.assertEqual(
            real_json_response["Content-Disposition"],
            f"attachment; filename={test_name}.json;",
        )

        for value in NOT_STRING_VALUES:
            wrong_response = get_response_with_file(value, value)

            self.assertEqual(
                wrong_response["Content-Type"], "application/json"
            )

            self.assertTrue(isinstance(wrong_response, FileResponse))
