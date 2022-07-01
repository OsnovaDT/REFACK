"""Business logic used in views"""

from django.http import JsonResponse

from refactoring.services.code_handler import CodeHandler
from refactoring.services.utils import get_error_if_code_invalid


def get_code_recommendations(code: bytes | str) -> dict:
    """Return refactoring recommendations for user's code"""

    recommendations = CodeHandler(code).recommendations

    return {
        rule: ", ".join(wrong_code_snippets)
        for rule, wrong_code_snippets in recommendations.items()
    }


def get_recommendations_or_error_response(code: bytes | str) -> JsonResponse:
    """Return response with recommendations or with error"""

    code_error = get_error_if_code_invalid(code)

    if code_error:
        results = {'error': code_error}
    else:
        results = {'recommendations': get_code_recommendations(code)}

    return JsonResponse(results)
