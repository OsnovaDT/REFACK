"""Class that parse the code and save it's modules

Code modules are: functions, classes, variables, etc.

"""

from collections import defaultdict
from ast import NodeVisitor, FunctionDef, Return, ClassDef, get_docstring

from refactoring.services.code_items import FunctionItem, ClassItem


def get_action_type(action: Return) -> str:
    """Return type of the code action"""

    try:
        action_value = action.value.value

        if isinstance(action_value, bool):
            action_type = 'return bool'
        else:
            action_type = 'return'
    except:
        action_type = ''

    return str(action_type)


def get_function_type(function_body: list) -> str:
    """Return type of function

    Types:
    1) return - function returns a value (exclude boolean):
        1. Has action with Return type
        2. Type of the action is not bool
    2) return bool - function returns boolean:
        1. Has action with Return type
        2. Type of the action is bool

    """

    function_type = ''

    for action in function_body:
        if isinstance(action, Return):
            # Обработка исключения для get_action_type
            function_type = get_action_type(action)

            break

    return function_type


class CodeParser(NodeVisitor):
    """Parse the code and save it's modules"""

    def __init__(self):
        self.__code_items = defaultdict(list)

    def visit_FunctionDef(self, function_definition: FunctionDef):
        """Parse function definition and add to all functions"""

        self.__code_items['functions'].append(
            FunctionItem({
                'name': function_definition.name,
                'type': get_function_type(function_definition.body),
                'docstring': get_docstring(function_definition),
                'type_hint': function_definition.returns,
                'args': function_definition.args.args,
            }),
        )

    def visit_ClassDef(self, class_definition: ClassDef):
        """Parse class definition and add to all classes"""

        self.__code_items['classes'].append(
            ClassItem({
                'name': class_definition.name,
                'docstring': get_docstring(class_definition),
            }),
        )

    @property
    def code_items(self) -> dict:
        """Return code modules"""

        return dict(self.__code_items)
