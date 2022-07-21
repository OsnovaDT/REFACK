"""Constants for testing refactoring app"""

from keyword import kwlist


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

INCORRECT_SNAKE_CASE_STRINGS = (
    'TEST', 'testTest', 'functionFunctionFunction', 'TEST_TEST', 'TestTest',
    'TEST_TEST_TEST', 'testTEST', 'tEsT', 'Test', 'tesT', 'A', 'B', ' ', '   ',
    'tesT1', 'test__test', 'test__', 'test___', 'test____test___test',
    '_test_',
) + KEYWORDS + NOT_STRING_VALUES + DIFFERENT_STRINGS

CORRECT_SNAKE_CASE_STRINGS = (
    'name', 'name123', 'super_long_name_12', 'super_long_name', 'car_color',
    'name_of_abuse', '_name', '__name', 'super_super_puper_long_name',
    'class_', 'list_', 'tuple_', 'set_', 'dict_', 'type_', 'get_value',
    'set_value', 'check_info', 'check',
)

# FOR TESTING services/utils.py

# For testing is_in_cap_words function

INCORRECT_CAP_WORDS_STRINGS = (
    'carEngine', 'car_Engine', 'superLongCarEngingeName',
    'superlongcarengingename',
) + CORRECT_SNAKE_CASE_STRINGS + KEYWORDS + NOT_STRING_VALUES \
  + DIFFERENT_STRINGS

CORRECT_CAP_WORDS_STRINGS = (
    'CarEngine', 'Car', 'SuperCar', 'SuperLongCarEngingeName',
)

# For testing function is_bool_function_correct

BOOL_FUNCTION_TYPE = 'bool'

CORRECT_BOOL_FUNCTIONS = (
    'is_correct', 'is_not_correct', 'is_value_set', 'is_value_not_set',
    'is_this_function_so_super_long',
)

INCORRECT_BOOL_FUNCTIONS = DIFFERENT_VALUES + (
    'Is_correct', 'IS_CORRECT', 'IsCorrect', 'isCorrect', 'isNotCorrect',
    'iS_value_correct', 'iSValueCorrect', 'isValueSet', 'isValueNotSet',
    'isThisFunctionSoSuperLong', 'isserverstart',

    'get_value', 'getValue',

    'is', 'IS', 'iS', 'Is', 'is_', 'IS_', 'iS_', 'Is_',

    'i', 's',
)

# For testing get_error_if_code_invalid

EXPECTED_INDENT_CLASS = \
    "expected an indented block after class definition on line 1"

EXPECTED_INDENT_FUNC = \
    "expected an indented block after function definition on line 1"

EXPECTED_COLON = "expected ':'"

UNEXPECTED_INDENT = "unexpected indent"

INVALID_SYNTAX = "invalid syntax"

CURLY_BRACE_WAS_NEVER_CLOSED = "'{' was never closed"

UNKNOWN_LINE = " (<unknown>, line "

UNKNOWN_LINE_1 = UNKNOWN_LINE + "1)"

UNKNOWN_LINE_2 = UNKNOWN_LINE + "2)"

# TODO Расширить
INVALID_CODE_AND_ERROR = {
    # Func
    "def": INVALID_SYNTAX + UNKNOWN_LINE_1,
    "def test()": EXPECTED_COLON + UNKNOWN_LINE_1,
    "def test():": EXPECTED_INDENT_FUNC + UNKNOWN_LINE_1,
    "def test():\nreturn 1": EXPECTED_INDENT_FUNC + UNKNOWN_LINE_2,
    "def test():\nreturn ": EXPECTED_INDENT_FUNC + UNKNOWN_LINE_2,
    "def test(:\n\treturn ": INVALID_SYNTAX + UNKNOWN_LINE_1,

    # Variable
    "a = ": INVALID_SYNTAX + UNKNOWN_LINE_1,
    " a = 1": UNEXPECTED_INDENT + UNKNOWN_LINE_1,
    "d = {": CURLY_BRACE_WAS_NEVER_CLOSED + UNKNOWN_LINE_1,

    # Class
    "class": INVALID_SYNTAX + UNKNOWN_LINE_1,
    "class: pass": INVALID_SYNTAX + UNKNOWN_LINE_1,
    "class A": EXPECTED_COLON + UNKNOWN_LINE_1,
    "class A:": EXPECTED_INDENT_CLASS + UNKNOWN_LINE_1,
    "class A:\npass": EXPECTED_INDENT_CLASS + UNKNOWN_LINE_2,
}

VALID_CODE = (
    "def test(): return 1", "def test(): return 'abc'", "class A: pass",
    "a = 10", "dict = {'a': 1, 'b': 2}",

    """
def test():
    return 1
    """,

    """
class A:
    def __init__(self):
        pass
    """,

    """
class Car:
    def __init__(self, color: str):
        self.color = color
    """,
)

# For testing function is_get_function_correct

NOT_BOOL_FUNCTION_TYPE = 'not bool'

CORRECT_GET_FUNCTIONS = (
    'get_value', 'get_value_from_object', 'get_very_super_long_user_login',
    'get_correct_value', 'get_incorrect_value',
)

INCORRECT_GET_FUNCTIONS = DIFFERENT_VALUES + (
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


TEST_REFACTORING_RESULTS = {
    'results': '{"Функции не начинаются с префикса «get»": "a",'
               '"Для функций не указана документация": "a",'
               '"Для функций не указан type hint": "a"}'
}
