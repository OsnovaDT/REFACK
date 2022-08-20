"""Utils for business logic"""

from re import fullmatch
from ast import NodeVisitor, parse

from refactoring.services.constants import (
    KEYWORDS, SNAKE_CASE_REGEXP, CAP_WORDS_REGEXP,
)


def get_code_error(code: str) -> str:
    """Return error if code is invalid else empty string"""

    error = ''

    if isinstance(code, str):
        try:
            NodeVisitor().visit(parse(code))
        except Exception as exception_error:
            error = str(exception_error)

    return error


def is_in_snake_case(string: str) -> bool:
    """True if the string has snake_case naming style"""

    is_in_snake_case_ = False

    if isinstance(string, str) and string not in KEYWORDS \
            and not (string.startswith('_') and string.endswith('_')):
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

    if isinstance(code, str):
        code = code.replace('\n', '<br>').replace(' ', '&nbsp;')

    return code


def get_code_items_without_duplicates(code_items: list | tuple) -> set:
    """Delete duplicates from code items.

    Of the duplicates, the ones announced below remain.

    """

    code_items_without_duplicates = set()

    if isinstance(code_items, (list, tuple)):
        code_items_without_duplicates = set(reversed(code_items))

    return code_items_without_duplicates
