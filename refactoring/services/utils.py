"""Utils for business logic"""

from ast import NodeVisitor, parse


def get_error_if_code_invalid(code: bytes | str) -> str | None:
    """Return error if code is invalid else None"""

    error = None

    try:
        NodeVisitor().visit(parse(code))
    except Exception as exception_error:
        error = str(exception_error)

    return error


def is_name_in_snake_case(name: str) -> bool:
    """True if the name has snake_case naming style"""

    return name.islower() and '_' in name


def is_name_in_cap_words(name: str) -> bool:
    """True if the name has CapWords naming style"""

    return not name.islower() \
        and not name.isupper() \
        and '_' not in name \
        and name[0].istitle()
