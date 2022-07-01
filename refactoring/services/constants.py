"""Constants of services app"""

# REFACTORING RULES

# Naming

PREFIX_GET = "Функции не начинаются с префикса «get»"

PREFIX_IS = "Функции не начинаются с префикса «is»"

# Naming style

SNAKE_CASE_STYLE = "Функции или методы не имеют стиль именования snake_case"

CAMEL_CASE_STYLE = "Классы не имеют стиль именования CamelCase"

# Documentation

FUNCTION_DOCUMENTATION = "Для функций не указана документация"

CLASS_DOCUMENTATION = "Для классов не указана документация"

# Type hint

FUNCTION_TYPE_HINT = "Для функций не указан type hint"

ARGUMENT_TYPE_HINT = "Для аргументов функций не указан type hint"


# TYPES OF RETURN COMMAND

BOOL_TYPE = 'bool'

NOT_BOOL_TYPE = 'not bool'


# NAMING STYLES

class NamingStyle:
    """Contain naming styles for functions, classes, methods, etc."""

    SNAKE_CASE = 'Snake Case'

    CAMEL_CASE = 'Camel case'
