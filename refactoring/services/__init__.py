"""Business logic used in views"""

from django.contrib.auth import get_user_model
from django.http import JsonResponse, FileResponse

from refactoring.models import RefactoringRecommendation
from refactoring.services.code_handler import CodeHandler
from refactoring.services.utils import (
    get_error_if_code_invalid, get_code_to_display_in_html,
    get_recommendation_to_display_in_html,
)
from refactoring.services.files_download import (
    get_response_with_file, get_xml_file_content,
)


User = get_user_model()


def get_recommendations_or_error_response(code: bytes | str) -> JsonResponse:
    """Return response with recommendations or with error"""

    code_error = get_error_if_code_invalid(code)

    if code_error:
        results = {'error': code_error}
    else:
        results = {'recommendations': _get_code_recommendations(code)}

    return JsonResponse(results)


def create_refactoring_recommendation(recommendation_data: dict) -> None:
    """Create refactoring recommendation"""

    RefactoringRecommendation.objects.create(
        user=User.objects.get(username=recommendation_data['username']),
        code=get_code_to_display_in_html(recommendation_data['code']),
        recommendation=get_recommendation_to_display_in_html(
            recommendation_data['recommendation'],
        ),
    )


def get_file_response_with_refactoring_recommendations(
        recommendations: str, extension: str) -> FileResponse | JsonResponse:
    """Return file response with refactoring recommendations"""

    if extension == 'xml':
        recommendations = get_xml_file_content(recommendations)

    return get_response_with_file(
        recommendations, 'refactoring_recommendations', extension,
    )


def _get_code_recommendations(code: bytes | str) -> dict:
    """Return refactoring recommendations for user's code"""

    recommendations = CodeHandler(code).recommendations

    return {
        rule: ", ".join(wrong_code_items)
        for rule, wrong_code_items in recommendations.items()
    }
