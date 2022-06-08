"""Constants for testing"""

class TestClass:
    """Empty class for testing"""


def test_function():
    """Empty function for testing"""


DIFFERENT_VALUES = (
    # Values of str and bytes type
    'value', 'value_value', 'value     value', '', '!@@#Q@$Q', 'test'.encode(),
    'a' * 100, 'a' * 10_000, '\n', '\t', 'class', 'def', 'int',

    # Values of int, float and bool types
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

# For function is_bool_function_correct

BOOL_FUNCTION_TYPE = 'return bool'

CORRECT_BOOL_FUNCTIONS = (
    'is_correct', 'is_not_correct', 'isCorrect', 'isNotCorrect',
    'is_value_set', 'is_value_not_set', 'isValueSet', 'isValueNotSet',
    'isThisFunctionSoSuperLong', 'is_this_function_so_super_long',
    'isserverstart',
)

INCORRECT_BOOL_FUNCTIONS = (
    'test', 'aaaaaaaaaaa', 'IS_CORRECT', '', 'IsCorrect', 'iSValueCorrect',
    'Is_correct', 'iS_value_correct', 'get_value', 'getValue',
    'check_function', 'is', 'i', 's', 'IS', 'iS', 'Is', 'is_', 'IS_',
    'iS_', 'Is_', 'a', 'b', 'A', 'B', '  '
) + DIFFERENT_VALUES

# For function is_get_function_correct

GET_FUNCTION_TYPE = 'return'

CORRECT_GET_FUNCTIONS = (
    'get_value', 'get_value_from_object', 'getValue', 'getValueFromObject',
    'get_correct_value', 'get_incorrect_value', 'getCorrectValue',
    'getIncorrectValue', 'get_very_super_long_user_login',
    'getVerySuperLongUserLogin', 'getvalue',
)

INCORRECT_GET_FUNCTIONS = (
    'test', 'aaaaaaaaaaa', 'GET_VALUE', '', 'GETValue', 'GET_value',
    'GetValue', 'gEtValue', 'geTValue', 'GEtValue', 'GeTValue', 'gETValue',
    'Get_value', 'gEt_value', 'geT_value', 'GEt_value', 'GeT_value',
    'gET_value', 'Getvalue', 'gEtvalue', 'geTvalue', 'GEtvalue', 'GeTvalue',
    'gETvalue', 'gEt_correct_value', 'is_correct', 'isCorrect',
    'isValueCorrect', 'check_function', 'get', 'g', 'e', 't',
    'GET', 'Get', 'gEt', 'geT', 'GeT', 'gET', 'get_', 'GET_',
    'Get_', 'gEt_', 'geT_', 'GeT_', 'gET_', 'a', 'b', 'A', 'B', '  '
) + DIFFERENT_VALUES
