"""Contain classes for code's items.

Code item is any code module. E.g. function or class.
It's used by code parser.

E.g. for function parser actions will be next:
1. Parser found the function in user's code;
2. It creates FunctionItem object with all function attributes;
3. Parser adds the object to all function items.

"""


class DefaultItem:
    """Default code item that is parent for all items classes"""

    def __init__(self, attributes: dict):
        self.__attributes = attributes

    def __repr__(self) -> str | None:
        return self.name

    def _get_attr(self, attr_name: str) -> str | list | None:
        """Return attr from item's attributes or None"""

        if attr_name in self.__attributes.keys():
            attr = self.__attributes[attr_name]
        else:
            attr = None

        return attr

    @property
    def name(self) -> str | None:
        """Item name"""

        return self._get_attr('name')

    @property
    def docstring(self) -> str | None:
        """Item docstring"""

        return self._get_attr('docstring')


class FunctionItem(DefaultItem):
    """Function item"""

    @property
    def type(self) -> str | None:
        """Function type.

        All possible types are in services/code_parser.py
        in «get_function_type» function.

        """

        return self._get_attr('type')

    @property
    def type_hint(self) -> str | None:
        """Function type hint"""

        return self._get_attr('type_hint')

    @property
    def args(self) -> list | None:
        """Function arguments"""

        return self._get_attr('args')


class ClassItem(DefaultItem):
    """Class item"""
