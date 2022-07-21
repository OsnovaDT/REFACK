"""Utils for business logic"""

from re import fullmatch
from ast import NodeVisitor, parse

from refactoring.services.constants import (
    KEYWORDS, SNAKE_CASE_REGEXP, CAP_WORDS_REGEXP,
)


def get_error_if_code_invalid(code: bytes | str) -> str | None:
    """Return error if code is invalid else None"""

    error = None

    try:
        NodeVisitor().visit(parse(code))
    except Exception as exception_error:
        error = str(exception_error)

    return error


def is_in_snake_case(string: str) -> bool:
    """True if the string has snake_case naming style"""

    is_in_snake_case_ = False

    if isinstance(string, str) \
            and string not in KEYWORDS \
            and not _is_starts_and_ends_with(string, '_'):
        is_in_snake_case_ = fullmatch(SNAKE_CASE_REGEXP, string) is not None

    return is_in_snake_case_


def is_in_cap_words(string: str) -> bool:
    """True if the name has CapWords naming style"""

    is_in_cap_words_ = False

    if isinstance(string, str) and string not in KEYWORDS:
        is_in_cap_words_ = fullmatch(CAP_WORDS_REGEXP, string) is not None

    return is_in_cap_words_


def get_code_to_display_in_html(code: str) -> str:
    """Convert and return code to display in HTML"""

    return code.replace('\n', '<br>').replace(' ', '&nbsp;')


def get_recommendation_to_display_in_html(recommendation: str) -> str:
    """Convert and return recommendation to display in HTML"""

    return recommendation.replace(
        ', ', '<br><br>'
    ).replace(
        '{', ''
    ).replace(
        '}', ''
    ).replace(
        "'", ''
    )


def _is_starts_and_ends_with(string: str, symbol: str) -> bool:
    """Check is string starts and ends with underscore"""

    is_starts_and_ends_with_ = False

    if isinstance(string, str) and isinstance(symbol, str):
        is_starts_and_ends_with_ = \
            string.startswith(symbol) and string.endswith(symbol)

    return is_starts_and_ends_with_
