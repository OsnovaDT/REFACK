"""Project middlewares"""

from traceback import format_exc
from typing import Callable, Any

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, FileResponse
from loguru import logger

from refactoring.services import (
    get_file_response_with_refactoring_recommendations,
)


logger.add(
    f"logs/{__name__}.log",
    level="ERROR",
    format=settings.LOG_FORMAT,
    rotation=settings.LOG_ROTATION,
    compression=settings.LOG_COMPRESSION,
)


class ExceptionHandlerMiddleware:
    """Handle exception"""

    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> Any:
        return self.get_response(request)

    def process_exception(
            self, request, exception) -> FileResponse | JsonResponse:
        """Process all exceptions"""

        logger.error(f"«{exception}»\n{format_exc()}")

        extention = request.resolver_match.kwargs.get('extention')

        if extention:
            response = get_file_response_with_refactoring_recommendations(
                request.POST['results'], extention,
            )
        else:
            response = JsonResponse({
                'error': 'Произошла внутренняя ошибка сервера',
                'recommendations': '',
            })

        return response
