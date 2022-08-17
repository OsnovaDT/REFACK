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
