"""Utils for main business logic functions"""

from ast import NodeVisitor, parse


def get_error_if_code_invalid(code: bytes | str) -> str | None:
    """Return error if code is invalid else None"""

    error = None

    try:
        NodeVisitor().visit(parse(code))
    except Exception as exception_error:
        error = str(exception_error)

    return error
