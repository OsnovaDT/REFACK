"""Parse user's code and save it's items.

For parsing uses module «ast».

Current code items:
1. Function (FunctionItem)
2. Class (ClassItem)

"""

from ast import ClassDef, get_docstring, FunctionDef, NodeVisitor, Pass, Return
from collections import defaultdict

from refactoring.services.code_items import ClassItem, FunctionItem
from refactoring.services.constants import BOOL_TYPE, NOT_BOOL_TYPE


class CodeParser(NodeVisitor):
    """Parse user's code and save it to code items"""

    def __init__(self):
        self.__code_items = defaultdict(list)

    @property
    def code_items(self) -> dict:
        """Return code items"""

        return dict(self.__code_items)

    def visit_FunctionDef(self, function_: FunctionDef) -> None:
        """Function parser.

        1. Create FunctionItem object for the function;
        2. Add it to all function items.

        """

        if isinstance(function_, FunctionDef):
            self.__code_items["functions"].append(
                FunctionItem({
                    "args": function_.args.args,
                    "docstring": get_docstring(function_),
                    "name": function_.name,
                    "type": self.__get_function_type(function_.body),
                    "type_hint": function_.returns,
                }),
            )

    def visit_ClassDef(self, class_: ClassDef) -> None:
        """Class parser.

        1. Create ClassItem object for the class;
        2. Add it to all class items.

        """

        if isinstance(class_, ClassDef):
            self.__code_items["classes"].append(
                ClassItem({
                    "docstring": get_docstring(class_),
                    "name": class_.name,
                }),
            )

    @staticmethod
    def __get_type_of_returned_code(returned_code: Return) -> str:
        """Return type of returned code.

        Possible types:
        1. bool (e.g. True, False);
        2. not bool (e.g. 1, 1.23, "Hello world").

        """

        if isinstance(returned_code, Return) \
                and isinstance(returned_code.value.value, bool):
            returned_code_type = BOOL_TYPE
        else:
            returned_code_type = NOT_BOOL_TYPE

        return returned_code_type

    def __get_function_type(self, function_body: list | tuple) -> str:
        """Return type of the function.

        Types:
        1. bool - function returns boolean;
        2. not bool - function returns not boolean;
        3. pass - function uses pass operator.

        """

        function_type = ""

        if isinstance(function_body, (list, tuple)):
            for action in function_body:
                if isinstance(action, Return):
                    function_type = self.__get_type_of_returned_code(action)

                    break

                if isinstance(action, Pass):
                    function_type = "pass"

        return function_type
