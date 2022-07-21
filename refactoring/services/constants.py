"""Constants of services app"""

from keyword import kwlist


# REFACTORING RULES

# Naming

PREFIX_GET = "Функции не начинаются с префикса «get»"

PREFIX_IS = "Функции не начинаются с префикса «is»"

# Naming style

SNAKE_CASE_STYLE = "Функции или методы не имеют стиль именования snake_case"

CAP_WORDS_STYLE = "Классы не имеют стиль именования CapWords"

# Documentation

FUNCTION_DOCSTRING = "Для функций не указана документация"

CLASS_DOCSTRING = "Для классов не указана документация"

# Type hint

FUNCTION_TYPE_HINT = "Для функций не указан type hint"

ARGUMENT_TYPE_HINT = "Для аргументов функций не указан type hint"


# TYPES OF RETURN COMMAND

BOOL_TYPE = 'bool'

NOT_BOOL_TYPE = 'not bool'

# OTHER

KEYWORDS = (
    'class', 'list', 'tuple', 'set', 'dict', 'arrow', 'str', 'int',
    'type', 'float',
) + tuple([str(kw) for kw in kwlist])

SNAKE_CASE_REGEXP = r"(_){,2}([a-z])([a-z0-9]{2,})(_[a-z0-9]{2,})*(_?)"

# CapWords regexp

ONE_CAP_WORD_REGEXP = r'([A-Z])([a-z0-9])+'

CAP_WORDS_REGEXP = ONE_CAP_WORD_REGEXP + '(' + ONE_CAP_WORD_REGEXP + r')*'
