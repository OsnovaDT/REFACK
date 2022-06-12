"""All constants"""

# Errors

COMMON_ERRORS = (AttributeError, TypeError,)

ERROR_PREFIX_GET = \
    "Функции должны начинаться с префикса «get»"

ERROR_PREFIX_IS = \
    "Функции должны начинаться с префикса «is»"

ERROR_SNAKE_CASE_FUNCTIONS = \
    "Функции и методы должны иметь стиль именования " \
    "Snake case (согласно PEP 8)"

ERROR_CAMEL_CASE_CLASSES = \
    "Классы должны иметь стиль именования Camel case (согласно PEP 8)"

ERROR_THERE_IS_NO_DOCUMENTATION_FOR_FUNCTION = \
    "Для этих функций должна быть указана документация"

ERROR_THERE_IS_NO_DOCUMENTATION_FOR_CLASS = \
    "Для этого класса должна быть указана документация"
