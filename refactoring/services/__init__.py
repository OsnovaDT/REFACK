"""Main business logic"""

from ast import NodeVisitor, parse

from django.http import JsonResponse

from refactoring.services.code_handler import CodeHandler


def get_code_recommendations(code: bytes | str) -> dict:
    """Return refactoring recommendations for user's code"""

    recommendations = CodeHandler(code).recommendations

    return {
        rule: ", ".join(wrong_code_snippets)
        for rule, wrong_code_snippets in recommendations.items()
    }


def _get_error_if_code_invalid(code: bytes | str) -> str | None:
    """Return error if code is invalid else None"""

    error = None

    try:
        NodeVisitor().visit(parse(code))
    except Exception as exception_error:
        error = str(exception_error)

    return error


def get_recommendations_or_error_response(code: bytes | str) -> JsonResponse:
    """Return response with recommendations or with error"""

    code_error = _get_error_if_code_invalid(code)

    if code_error:
        results = {'error': code_error}
    else:
        results = {'recommendations': get_code_recommendations(code)}

    return JsonResponse(results)
