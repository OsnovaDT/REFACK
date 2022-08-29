"""Project middlewares"""

from traceback import format_exc
from typing import Any, Callable

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, JsonResponse
from loguru import logger

from refactoring.services import (
    get_file_response_with_refactoring_recommendations,
)


logger.add(
    f"logs/{__name__}.log",
    compression=settings.LOG_COMPRESSION,
    format=settings.LOG_FORMAT,
    level="ERROR",
    rotation=settings.LOG_ROTATION,
)


class ExceptionHandlerMiddleware:
    """Handle any exception"""

    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> Any:
        return self.get_response(request)

    def process_exception(
            self, request, exception) -> FileResponse | JsonResponse:
        """Process all exceptions"""

        logger.error(f"«{exception}»\n{format_exc()}")

        if extention := request.resolver_match.kwargs.get("extention"):
            response = get_file_response_with_refactoring_recommendations(
                request.POST["results"],
                extention,
            )
        else:
            response = JsonResponse({
                "error": "Произошла внутренняя ошибка сервера",
                "recommendations": "",
            })

        return response
