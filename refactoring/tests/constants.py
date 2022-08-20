"""Constants for testing refactoring app"""

from keyword import kwlist
from ast import Name, arg

from refactoring.services.code_items import FunctionItem, ClassItem


def get_arg_type_hint_error(argument: str, func_name: str) -> str:
    """Return argument type hint error with replaced values"""

    return f'аргумент «{argument}» (функция «{func_name}»)'


# Common constants


class TestClass:
    """Empty class for testing"""


def test_function():
    """Empty function for testing"""


KEYWORDS = (
    'class', 'list', 'tuple', 'set', 'dict', 'arrow', 'str', 'int',
    'type', 'float',
) + tuple([str(keyword) for keyword in kwlist])

NOT_STRING_VALUES = (
    # int, float and bool
    0, 100_000, -100, 122.12323, True, False,

    # Data structures
    [1, 2, 3], (1, 2), {'a': 1, 'b': 2}, set([1, 2, 3]), [[1, 2, 3, (1, 2)]],

    # Types
    int, bool, str, object, bytes, bytearray, tuple, list, dict, set, float,

    # Classes and functions
    TestClass, test_function, lambda x: x,

    # Others
    None, complex(1, 2), bin(20), hex(100), range(100),
)

DIFFERENT_STRINGS = (
    'value     value', '', '!@@#Q@$Q', 'test'.encode(), 'a', 'b', 'A', 'B',
    '', '  ', '\n', '\t', 'def'
)

DIFFERENT_VALUES = DIFFERENT_STRINGS + NOT_STRING_VALUES

# For testing is_in_snake_case function

INCORRECT_SNAKE_CASE_NAMES = (
    'TEST', 'testTest', 'functionFunctionFunction', 'TEST_TEST', 'TestTest',
    'TEST_TEST_TEST', 'testTEST', 'tEsT', 'Test', 'tesT', 'A', 'B', ' ', '   ',
    'tesT1', 'test__test', 'test__', 'test___', 'test____test___test',
    '_test_',
)

INCORRECT_SNAKE_CASE_STRINGS = INCORRECT_SNAKE_CASE_NAMES \
    + KEYWORDS + NOT_STRING_VALUES + DIFFERENT_STRINGS

CORRECT_SNAKE_CASE_STRINGS = (
    'name', 'name123', 'super_long_name_12', 'super_long_name', 'car_color',
    'name_of_abuse', '_name', '__name', 'super_super_puper_long_name',
    'class_', 'list_', 'tuple_', 'set_', 'dict_', 'type_', 'get_value',
    'set_value', 'check_info', 'check',
)

# For testing is_in_cap_words function

INCORRECT_CAP_WORDS_NAMES = (
    'carEngine', 'car_Engine', 'superLongCarEngingeName',
    'superlongcarengingename',
)

INCORRECT_CAP_WORDS_STRINGS = INCORRECT_CAP_WORDS_NAMES \
    + CORRECT_SNAKE_CASE_STRINGS \
    + KEYWORDS \
    + NOT_STRING_VALUES \
    + DIFFERENT_STRINGS

CORRECT_CAP_WORDS_STRINGS = (
    'CarEngine', 'Car', 'SuperCar', 'SuperLongCarEngingeName',
)

# For testing function is_bool_function_correct

BOOL_FUNCTION_TYPE = 'bool'


NOT_BOOL_FUNCTION_TYPE = 'not bool'


TEST_REFACTORING_RESULTS = {
    'results': '{"Функции не начинаются с префикса «get»": "a",'
               '"Для функций не указана документация": "a",'
               '"Для функций не указан type hint": "a"}'
}

# For testing function get_code_error

VALID_CODES = (
    """
def test1():
    pass
    """,

    """
class TestClass:
    pass
    """,

    """
class TestClass:
    def __init__(self, value):
        self.value = value
    """,

    """
from django.test import TestCase, tag
    """,

    """
def get_value(value):
    return value

def is_correct():
    return True
    """,

    """
var1 = 10
var2 = 1
print(var1 + var2)
    """,
)

INVALID_CODES_AND_ERROR = {
    """
def test1()
    pass
    """: "expected ':' (<unknown>, line 2)",

    """
def test1(
    pass
    """: "'(' was never closed (<unknown>, line 2)",

    """
def test1
    pass
    """: "invalid syntax (<unknown>, line 2)",

    """def test1():""": "expected an indented block after function "
                        "definition on line 1 (<unknown>, line 1)",
    """def""": "invalid syntax (<unknown>, line 1)",

    """class""": "invalid syntax (<unknown>, line 1)",
    """class A""": "expected ':' (<unknown>, line 1)",
    """class A:""": "expected an indented block after class definition "
                    "on line 1 (<unknown>, line 1)",

    """from""": "invalid syntax (<unknown>, line 1)",
    """import""": "invalid syntax (<unknown>, line 1)",
    """from re import""": "invalid syntax (<unknown>, line 1)",

    """a =""": "invalid syntax (<unknown>, line 1)",
    """a = [""": "'[' was never closed (<unknown>, line 1)",
    """a = (""": "'(' was never closed (<unknown>, line 1)",
    """a = {""": "'{' was never closed (<unknown>, line 1)",
    """a = {'""": "unterminated string literal (detected at line 1) "
                  "(<unknown>, line 1)",
    """a = {'a'""": "'{' was never closed (<unknown>, line 1)",
    """a = {'a':""": "'{' was never closed (<unknown>, line 1)",
    """a = {'a': 10""": "'{' was never closed (<unknown>, line 1)",
    """print('test'""": "'(' was never closed (<unknown>, line 1)",
}

# For testing function get_code_to_display_in_html

CODE_AND_HTML_CODE = {
    'def test():\n\tpass': 'def&nbsp;test():<br>\tpass',

    'class A:\ndef __init__(self):\npass':
        'class&nbsp;A:<br>def&nbsp;__init__(self):<br>pass',

    'from os import getcwd': 'from&nbsp;os&nbsp;import&nbsp;getcwd',
}

# services.rules_checker.py

STR_TYPE_HINT = Name(id='str')

INT_TYPE_HINT = Name(id='int')

BOOL_TYPE_HINT = Name(id='bool')

CALLABLE_TYPE_HINT = Name(id='Callable')

NONE_TYPE_HINT = Name(id='None')

# For testing TypeHintCheckerMixin mixin

# For testing _check_functions_args_have_type_hints method

FUNCTIONS_WITH_CORRECT_ARG_TYPE_HINT = (
    FunctionItem({
        'name': 'get_value',
        'type': 'not bool',
        'type_hint': 'str',
        'args': [
            arg(arg='value', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'get_value_2',
        'type': 'not bool',
        'docstring': 'Return value',
        'args': [
            arg(arg='value1', annotation=INT_TYPE_HINT),
            arg(arg='value2', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'get_value_3',
        'type': 'not bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2', annotation=INT_TYPE_HINT),
            arg(arg='value3', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'is_correct_data',
        'type': 'bool',
        'type_hint': 'bool',
        'args': [],
    }),

    FunctionItem({
        'name': 'check_data',
        'type': 'pass',
        'docstring': 'Check data',
        'type_hint': 'bool',
        'args': [],
    }),
)

FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT_ERRORS = sorted([
    # When there is no any arguments

    # 1 function
    get_arg_type_hint_error("value", "get_value"),
    # 'аргумент «value» (функция «get_value»)',

    # 2 function
    get_arg_type_hint_error("value1", "get_value_2"),
    get_arg_type_hint_error("value2", "get_value_2"),

    # 2 function
    get_arg_type_hint_error("value1", "get_value_3"),
    get_arg_type_hint_error("value2", "get_value_3"),
    get_arg_type_hint_error("value3", "get_value_3"),

    # When 1-st there is

    # 1 function
    get_arg_type_hint_error("value2", "check_data_1"),
    get_arg_type_hint_error("value3", "check_data_1"),

    # 2 function

    get_arg_type_hint_error("value2", "check_data_2"),

    # 3 function

    get_arg_type_hint_error("value3", "check_data_3"),

    # When 2-nd there is

    # 1 function
    get_arg_type_hint_error("value1", "is_correct_1"),
    get_arg_type_hint_error("value3", "is_correct_1"),

    # 2 function
    get_arg_type_hint_error("value3", "is_correct_2"),

    # 3 function
    get_arg_type_hint_error("value1", "is_correct_3"),

    # When 3-rd there is

    # 1 function
    get_arg_type_hint_error("value1", "is_correct_4"),
    get_arg_type_hint_error("value2", "is_correct_4"),

    # 2 function
    get_arg_type_hint_error("value1", "check_data_4"),

    # 3 function
    get_arg_type_hint_error("value2", "get_value_4"),
])

FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT = (
    # When there is no any arguments

    FunctionItem({
        'name': 'get_value',
        'type': 'not bool',
        'type_hint': 'str',
        'docstring': 'Return value',
        'args': [
            arg(arg='value'),
        ],
    }),

    FunctionItem({
        'name': 'get_value_2',
        'type': 'not bool',
        'args': [
            arg(arg='value1'),
            arg(arg='value2'),
        ],
    }),

    FunctionItem({
        'name': 'get_value_3',
        'type': 'not bool',
        'args': [
            arg(arg='value1'),
            arg(arg='value2'),
            arg(arg='value3'),
        ],
    }),

    # When 1-st there is

    FunctionItem({
        'name': 'check_data_1',
        'type': 'pass',
        'type_hint': 'bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
            arg(arg='value3'),
        ],
    }),

    FunctionItem({
        'name': 'check_data_2',
        'type': 'pass',
        'type_hint': 'bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
            arg(arg='value3', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'check_data_3',
        'type': 'pass',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2', annotation=INT_TYPE_HINT),
            arg(arg='value3'),
        ],
    }),

    # When 2-nd there is

    FunctionItem({
        'name': 'is_correct_1',
        'type': 'bool',
        'docstring': 'Docstring',
        'args': [
            arg(arg='value1'),
            arg(arg='value2', annotation=INT_TYPE_HINT),
            arg(arg='value3'),
        ],
    }),

    FunctionItem({
        'name': 'is_correct_2',
        'type': 'bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2', annotation=INT_TYPE_HINT),
            arg(arg='value3'),
        ],
    }),

    FunctionItem({
        'name': 'is_correct_3',
        'type': 'bool',
        'args': [
            arg(arg='value1'),
            arg(arg='value2', annotation=INT_TYPE_HINT),
            arg(arg='value3', annotation=STR_TYPE_HINT),
        ],
    }),

    # When 3-rd there is

    FunctionItem({
        'name': 'is_correct_4',
        'type': 'bool',
        'args': [
            arg(arg='value1'),
            arg(arg='value2'),
            arg(arg='value3', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'check_data_4',
        'type': 'pass',
        'args': [
            arg(arg='value1'),
            arg(arg='value2', annotation=INT_TYPE_HINT),
            arg(arg='value3', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'get_value_4',
        'type': 'not bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
            arg(arg='value3', annotation=STR_TYPE_HINT),
        ],
    }),
)

ARGUMENT_TYPE_HINT = "Для аргументов функций не указан type hint"

FUNCTIONS_WITH_ARGS = FUNCTIONS_WITH_CORRECT_ARG_TYPE_HINT + \
    FUNCTIONS_WITH_INCORRECT_ARG_TYPE_HINT

# For testing _check_functions_have_type_hint method

FUNCTIONS_WITH_TYPE_HINT = (
    FunctionItem({
        'name': 'get_value',
        'type': 'not bool',
        'type_hint': STR_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'get_value_2',
        'type': 'not bool',
        'type_hint': INT_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'is_correct',
        'type': 'bool',
        'type_hint': BOOL_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'get_func',
        'type': 'not bool',
        'type_hint': CALLABLE_TYPE_HINT,
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'get_func_2',
        'type': 'not bool',
        'type_hint': CALLABLE_TYPE_HINT,
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
        ],
    }),
)

FUNCTIONS_WITHOUT_TYPE_HINT = (
    FunctionItem({
        'name': 'get_value_without_type_hint',
        'type': 'not bool'
    }),

    FunctionItem({
        'name': 'check_value_without_type_hint',
        'type': 'pass'
    }),

    FunctionItem({
        'name': 'is_correct_without_type_hint',
        'type': 'bool'
    }),

    FunctionItem({
        'name': 'is_correct_without_type_hint_2',
        'docstring': 'Docstring',
        'type': 'bool'
    }),

    FunctionItem({
        'name': 'get_func_without_type_hint',
        'type': 'not bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2', annotation=STR_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'get_func_without_type_hint_2',
        'type': 'not bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
        ],
    }),
)

FUNCTION_TYPE_HINT = "Для функций не указан type hint"

# For testing DocstringCheckerMixin mixin

# For testing _check_functions_and_classes_have_docstring method

# Functions

FUNCTIONS_WITH_DOCSTRING = (
    FunctionItem({
        'name': 'get_value_1',
        'type': 'not bool',
        'docstring': 'Return value 1',
    }),

    FunctionItem({
        'name': 'get_value_2',
        'type': 'not bool',
        'docstring': 'Return value 2',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'get_value_3',
        'type': 'not bool',
        'docstring': 'Return value 3',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
        ],
    }),

    FunctionItem({
        'name': 'get_value_4',
        'type': 'not bool',
        'docstring': 'Return value 4',
        'type_hint': STR_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'get_value_5',
        'type': 'not bool',
        'docstring': 'Return value 5',
        'type_hint': INT_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'is_value_correct',
        'type': 'bool',
        'docstring': 'Check is value correct',
        'type_hint': BOOL_TYPE_HINT,
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
        ],
    }),

    FunctionItem({
        'name': 'check_value',
        'type': 'pass',
        'docstring': 'Check value',
        'type_hint': NONE_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'get_func',
        'type': 'not bool',
        'docstring': 'Return value',
        'type_hint': CALLABLE_TYPE_HINT,
    }),
)

FUNCTIONS_WITHOUT_DOCSTRING = (
    FunctionItem({
        'name': 'get_value_1',
        'type': 'not bool',
    }),

    FunctionItem({
        'name': 'get_value_2',
        'type': 'not bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
        ],
    }),

    FunctionItem({
        'name': 'get_value_3',
        'type': 'not bool',
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
        ],
    }),

    FunctionItem({
        'name': 'get_value_4',
        'type': 'not bool',
        'type_hint': STR_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'get_value_5',
        'type': 'not bool',
        'type_hint': INT_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'is_value_correct',
        'type': 'bool',
        'type_hint': BOOL_TYPE_HINT,
        'args': [
            arg(arg='value1', annotation=BOOL_TYPE_HINT),
            arg(arg='value2'),
        ],
    }),

    FunctionItem({
        'name': 'check_value',
        'type': 'pass',
        'type_hint': NONE_TYPE_HINT,
    }),

    FunctionItem({
        'name': 'get_func',
        'type': 'not bool',
        'type_hint': CALLABLE_TYPE_HINT,
    }),
)

FUNCTION_DOCSTRING = "Для функций не указана документация"

# Classes

CLASSES_WITH_DOCSTRING = (
    ClassItem({
        'name': 'CarEngine',
        'docstring': 'Class for car engine',
    }),

    ClassItem({
        'name': 'SuperCarEngine',
        'docstring': 'Class for super car engine',
    }),
)

CLASSES_WITHOUT_DOCSTRING = (
    ClassItem({'name': 'CarEngine'}),
    ClassItem({'name': 'SuperCarEngine'}),
)

CLASS_DOCSTRING = "Для классов не указана документация"

# For testing NamingStyleCheckerMixin mixin

# For testing _check_functions_naming_style_is_snake_case method

CORRECT_SNAKE_CASE_FUNCTIONS = [
    FunctionItem({'name': name, 'type': 'not bool'})
    for name in CORRECT_SNAKE_CASE_STRINGS
]

INCORRECT_SNAKE_CASE_FUNCTIONS = [
    FunctionItem({'name': name, 'type': 'not bool'})
    for name in CORRECT_CAP_WORDS_STRINGS
]

SNAKE_CASE_STYLE = "Функции или методы не имеют стиль именования snake_case"

# For testing _check_classes_naming_style_is_cap_words method

CORRECT_CAP_WORDS_CLASSES = [
    ClassItem({'name': name, 'type': 'not bool'})
    for name in CORRECT_CAP_WORDS_STRINGS
]

INCORRECT_CAP_WORDS_CLASSES = [
    ClassItem({'name': name, 'type': 'not bool'})
    for name in INCORRECT_CAP_WORDS_NAMES
]

CAP_WORDS_STYLE = "Классы не имеют стиль именования CapWords"

# For testing NamingCheckerMixin mixin

# For testing _check_not_bool_functions_start_with_get method

CORRECT_GET_NAMES = (
    'get_value', 'get_value_from_object', 'get_very_super_long_user_login',
    'get_correct_value', 'get_incorrect_value',
)

INCORRECT_GET_NAMES = (
    'GETValue', 'GEtvalue', 'GEtValue',
    'GetValue', 'GeTvalue', 'Getvalue', 'GeTValue',

    'gETvalue', 'gEtvalue', 'geTvalue', 'gEtValue', 'geTValue', 'gETValue',
    'getValue', 'getValueFromObject', 'getCorrectValue', 'getIncorrectValue',
    'getVerySuperLongUserLogin', 'getvalue',

    'GET_value', 'GET_VALUE', 'Get_value', 'gEt_value', 'geT_value',
    'GEt_value', 'GeT_value', 'gET_value', 'gEt_correct_value',

    'is_correct', 'isCorrect', 'isValueCorrect',

    'get', 'GET', 'Get', 'gEt', 'geT', 'GeT', 'gET', 'get_', 'GET_', 'Get_',
    'gEt_', 'geT_', 'GeT_', 'gET_',

    'g', 'e', 't',
)

CORRECT_GET_FUNCTIONS = [
    FunctionItem({'name': name, 'type': 'not bool'})
    for name in CORRECT_GET_NAMES
]

INCORRECT_GET_FUNCTIONS = [
    FunctionItem({'name': name, 'type': 'not bool'})
    for name in INCORRECT_GET_NAMES
]

PREFIX_GET = "Функции не начинаются с префикса «get»"

# For testing _check_bool_functions_start_with_is method

CORRECT_BOOL_NAMES = (
    'is_correct', 'is_not_correct', 'is_value_set', 'is_value_not_set',
    'is_this_function_so_super_long',
)

INCORRECT_BOOL_NAMES = (
    'Is_correct', 'IS_CORRECT', 'IsCorrect', 'isCorrect', 'isNotCorrect',
    'iS_value_correct', 'iSValueCorrect', 'isValueSet', 'isValueNotSet',
    'isThisFunctionSoSuperLong', 'isserverstart',

    'get_value', 'getValue',

    'is', 'IS', 'iS', 'Is', 'is_', 'IS_', 'iS_', 'Is_',

    'i', 's',
)

CORRECT_BOOL_FUNCTIONS = [
    FunctionItem({'name': name, 'type': 'bool'})
    for name in CORRECT_BOOL_NAMES
]

INCORRECT_BOOL_FUNCTIONS = [
    FunctionItem({'name': name, 'type': 'bool'})
    for name in INCORRECT_BOOL_NAMES
]

PREFIX_IS = "Функции не начинаются с префикса «is»"
