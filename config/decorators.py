"""Decorators of the project"""

from functools import wraps
from traceback import format_exc

from django.http import JsonResponse
from loguru import logger


def catch_json_response_exception(func):
    """Decorator for catching exception in JsonResponse view"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except Exception as exception:
            logger.error(f"«{exception}»\n{format_exc()}")

            response = JsonResponse({
                'error': 'Произошла внутренняя ошибка сервера',
                'recommendations': '',
            })

        return response

    return wrapper
