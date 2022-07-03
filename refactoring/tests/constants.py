"""Constants for testing refactoring app"""


class TestClass:
    """Empty class for testing"""


def test_function():
    """Empty function for testing"""


DIFFERENT_VALUES = (
    # str and bytes
    'test', 'aaaaaaaaaaa', 'check_function',
    'value', 'value_value', 'value     value', '', '!@@#Q@$Q', 'test'.encode(),
    'a', 'b', 'A', 'B', '', '  ',
    'a' * 100, 'a' * 10_000, '\n', '\t', 'class', 'def', 'int',

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
