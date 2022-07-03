"""Parse user's code and save it's items.

For parsing uses «ast» module.

Code items:
1. Function (FunctionItem);
2. Class (ClassItem).

"""

from collections import defaultdict
from ast import (
    NodeVisitor, FunctionDef, Return, ClassDef, get_docstring, Pass
)

from refactoring.services.code_items import FunctionItem, ClassItem
from refactoring.services.constants import BOOL_TYPE, NOT_BOOL_TYPE


class CodeParser(NodeVisitor):
    """Parse user's code, save and return it's items"""

    def __init__(self):
        self.__code_items = defaultdict(list)

    @staticmethod
    def __get_type_of_return(return_: Return) -> str:
        """Get type of code returned.

        Types:
        1. bool (e.g. return True, return False);
        2. not bool (e.g. return 1, return 1.23, return "string").

        """

        value_of_return = return_.value.value

        if isinstance(value_of_return, bool):
            type_of_return = BOOL_TYPE
        else:
            type_of_return = NOT_BOOL_TYPE

        return type_of_return

    def __get_function_type(self, function_body: list) -> str:
        """Return type of the function.

        Types:
        1. bool - function returns boolean;
        2. not bool - function returns not boolean;
        3. pass - function uses pass operator.

        """

        function_type = ''

        for action in function_body:
            if isinstance(action, Return):
                function_type = self.__get_type_of_return(action)

                break

            if isinstance(action, Pass):
                function_type = 'pass'

        return function_type

    def visit_FunctionDef(self, function: FunctionDef) -> None:
        """Function parser.

        1. Create FunctionItem object for the function;
        2. Add it to all function items.

        """

        self.__code_items['functions'].append(
            FunctionItem({
                'name': function.name,
                'type': self.__get_function_type(function.body),
                'docstring': get_docstring(function),
                'type_hint': function.returns,
                'args': function.args.args,
            }),
        )

    def visit_ClassDef(self, class_: ClassDef) -> None:
        """Class parser.

        1. Create ClassItem object for the class;
        2. Add it to all class items.

        """

        self.__code_items['classes'].append(
            ClassItem({
                'name': class_.name,
                'docstring': get_docstring(class_),
            }),
        )

    @property
    def code_items(self) -> dict:
        """Return code items"""

        return dict(self.__code_items)
