"""Tests for services.__init__ module"""

from json import loads

from django.contrib.auth import get_user_model
from django.http import FileResponse, JsonResponse
from django.test import tag, TestCase

from refactoring.models import RefactoringRecommendation
from refactoring.services import (
    create_refactoring_recommendation,
    get_file_with_refactoring_recommendations,
    get_recommendations_or_error_response,
    _get_code_recommendations,
)
from refactoring.tests.constants import (
    CODE_AND_ERROR,
    CODE_AND_RECOMMENDATIONS,
    FILE_CONTENT,
    NOT_STRING_VALUES,
    REFACTORING_RECOMMENDATION_DATA,
)


User = get_user_model()


@tag("refactoring_services", "refactoring_services_init")
class FunctionsTests(TestCase):
    """Test module functions"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_user_name = "test"

        User.objects.create(username=cls.test_user_name, password="1234")

    def test_create_refactoring_recommendation(self) -> None:
        """Test create_refactoring_recommendation function"""

        self.assertEqual(RefactoringRecommendation.objects.count(), 0)

        create_refactoring_recommendation(REFACTORING_RECOMMENDATION_DATA)

        self.assertEqual(RefactoringRecommendation.objects.count(), 1)

        recommendation = RefactoringRecommendation.objects.last()

        self.assertEqual(
            recommendation.recommendation,
            REFACTORING_RECOMMENDATION_DATA["recommendation"],
        )

        self.assertEqual(
            recommendation.user,
            User.objects.get(username=self.test_user_name),
        )

        self.assertEqual(
            recommendation.code,
            REFACTORING_RECOMMENDATION_DATA["code"]
            .replace("\n", "<br>")
            .replace(" ", "&nbsp;"),
        )

        # Empty data

        create_refactoring_recommendation({})

        self.assertEqual(RefactoringRecommendation.objects.count(), 1)

        # Invalid data

        create_refactoring_recommendation(100)

        self.assertEqual(RefactoringRecommendation.objects.count(), 1)

    def test_get_file_response_with_refactoring_recommendations(self) -> None:
        """Test get_file_with_refactoring_recommendations function"""

        # PDF and XML

        for extension in ("pdf", "xml"):
            pdf_response = get_file_with_refactoring_recommendations(
                FILE_CONTENT,
                extension,
            )

            self.assertTrue(isinstance(pdf_response, FileResponse))

            self.assertEqual(
                pdf_response["Content-Type"],
                f"application/{extension}",
            )

            self.assertEqual(
                pdf_response["Content-Disposition"],
                "attachment; filename="
                f"refactoring_recommendations.{extension};",
            )

        # JSON

        json_response = get_file_with_refactoring_recommendations(
            FILE_CONTENT,
            "json",
        )

        expected_json_response = JsonResponse(
            loads(FILE_CONTENT),
            json_dumps_params={"ensure_ascii": False},
        )

        self.assertTrue(isinstance(json_response, JsonResponse))

        self.assertEqual(
            json_response.__dict__["_container"],
            expected_json_response.__dict__["_container"],
        )

        self.assertEqual(json_response["Content-Type"], "application/json")

        self.assertEqual(
            json_response["Content-Disposition"],
            "attachment; filename=refactoring_recommendations.json;",
        )

        # Wrong values

        for value in NOT_STRING_VALUES:
            wrong_response = get_file_with_refactoring_recommendations(
                value, value
            )

            self.assertEqual(
                wrong_response["Content-Type"], "application/json"
            )

            self.assertTrue(isinstance(wrong_response, FileResponse))

    def test_get_code_recommendations(self) -> None:
        """Test _get_code_recommendations function"""

        for code, expected_recommendations in CODE_AND_RECOMMENDATIONS.items():
            self.assertEqual(
                _get_code_recommendations(code),
                expected_recommendations,
            )

        for code, error_and_message in CODE_AND_ERROR.items():
            error, message = error_and_message

            with self.assertRaisesMessage(error, message):
                _get_code_recommendations(code)

        for value in NOT_STRING_VALUES:
            self.assertEqual(_get_code_recommendations(value), {})

    def test_get_recommendations_or_error_response(self) -> None:
        """Test get_recommendations_or_error_response function"""

        for code in tuple(CODE_AND_RECOMMENDATIONS) + NOT_STRING_VALUES:
            response = get_recommendations_or_error_response(code)

            self.assertNotEqual(response._container, 0)
            self.assertEqual(response.status_code, 200)

            self.assertIn(b"recommendations", response._container[0])
            self.assertNotIn(b"error", response._container[0])

            self.assertTrue(isinstance(response, JsonResponse))
            self.assertEqual(response["Content-Type"], "application/json")

        for code in CODE_AND_ERROR:
            response = get_recommendations_or_error_response(code)

            self.assertNotEqual(response._container, 0)
            self.assertEqual(response.status_code, 200)

            self.assertIn(b"error", response._container[0])
            self.assertNotIn(b"recommendations", response._container[0])

            self.assertTrue(isinstance(response, JsonResponse))
            self.assertEqual(response["Content-Type"], "application/json")
