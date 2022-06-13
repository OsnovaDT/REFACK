"""Utils for refactoring app"""

from logging import getLogger

from refactoring.code_inspector import CodeInspector


def get_code_errors(code: bytes | str) -> dict | str:
    """Return errors for request's code"""

    try:
        code_errors = CodeInspector(code).errors

        for key, value in code_errors.items():
            code_errors[key] = ", ".join(value)

        if len(code_errors) == 0:
            code_errors = 'Ваш код чистый!'
    except Exception as error:
        getLogger().error(f'Error: {error}')
        code_errors = {}

    return code_errors
