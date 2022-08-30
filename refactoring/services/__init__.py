"""Business logic used in views"""

from ast import parse

from django.contrib.auth import get_user_model
from django.http import FileResponse, JsonResponse

from refactoring.models import RefactoringRecommendation
from refactoring.services.code_parser import CodeParser
from refactoring.services.files_download import (
    get_response_with_file,
    get_xml_file_content,
)
from refactoring.services.rules_checker import CleanCodeRulesChecker
from refactoring.services.utils import (
    get_code_error,
    get_code_to_display_in_html,
)


User = get_user_model()


def create_refactoring_recommendation(recommendation_data: dict) -> None:
    """Create refactoring recommendation"""

    if isinstance(recommendation_data, dict):
        code = recommendation_data.get("code")
        recommendation = recommendation_data.get("recommendation")
        username = recommendation_data.get("username")

        if code and recommendation and username:
            RefactoringRecommendation.objects.create(
                user=User.objects.get(username=username),
                recommendation=recommendation,
                code=get_code_to_display_in_html(code),
            )


def get_file_with_refactoring_recommendations(
        recommendations: str,
        file_extension: str) -> FileResponse | JsonResponse:
    """Return file response with refactoring recommendations"""

    if file_extension == "xml":
        recommendations = get_xml_file_content(recommendations)

    return get_response_with_file(
        recommendations,
        f"refactoring_recommendations.{file_extension}",
    )


def get_recommendations_or_error_response(code: str) -> JsonResponse:
    """Return response with recommendations or with error"""

    code_error = get_code_error(code)

    if code_error != "":
        response_data = {"error": code_error}
    else:
        response_data = {"recommendations": _get_code_recommendations(code)}

    return JsonResponse(response_data)


def _get_code_recommendations(code: str) -> dict:
    """Return refactoring recommendations for the code"""

    code_recommendations = {}

    if isinstance(code, str):
        parser = CodeParser()
        parser.visit(parse(code))

        recommendations = CleanCodeRulesChecker(
            parser.code_items,
        ).recommendations

        code_recommendations = {
            rule: ", ".join(wrong_code_items)
            for rule, wrong_code_items in recommendations.items()
        }

    return code_recommendations
