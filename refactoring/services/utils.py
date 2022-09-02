"""Utils for services app"""

from ast import NodeVisitor, parse
from re import fullmatch

from refactoring.services.constants import (
    CAP_WORDS_REGEXP,
    KEYWORDS,
    SNAKE_CASE_REGEXP,
)


def get_code_error(code: str) -> str:
    """Return error if code is invalid else empty string"""

    error = ""

    if isinstance(code, str):
        try:
            NodeVisitor().visit(parse(code))
        except Exception as exception_error:
            error = str(exception_error)

    return error


def is_in_snake_case(string: str) -> bool:
    """True if the string has snake_case naming style"""

    is_in_snake_case_ = False

    if (isinstance(string, str)
            and string not in KEYWORDS
            and not (
                string.startswith("_") and string.endswith("_")
            )):
        is_in_snake_case_ = fullmatch(SNAKE_CASE_REGEXP, string) is not None

    return is_in_snake_case_


def is_in_cap_words(string: str) -> bool:
    """True if the string has CapWords naming style"""

    is_in_cap_words_ = False

    if isinstance(string, str) and string not in KEYWORDS:
        is_in_cap_words_ = fullmatch(CAP_WORDS_REGEXP, string) is not None

    return is_in_cap_words_


def get_code_to_display_in_html(code: str) -> str:
    """Convert and return code for HTML displaying"""

    if isinstance(code, str):
        code = code.replace("\n", "<br>").replace(" ", "&nbsp;")

    return code


def get_code_items_without_duplicates(code_items: list | tuple) -> set:
    """Delete duplicates from code items.

    For equal items will be removed that is upper.

    """

    code_items_without_duplicates = set()

    if isinstance(code_items, (list, tuple)):
        code_items_without_duplicates = set(reversed(code_items))

    return code_items_without_duplicates
