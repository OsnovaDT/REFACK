"""Contain classes for code's items.

Code item is any code module. E.g. function, variable, class, etc.
It's used by code parser.

E.g. for function parser actions will be next:
1. Parser found the function in user's code;
2. It creates FunctionItem object with all function attributes;
3. Parser adds the object to all function items.

"""


class DefaultItem:
    """Default code item that is parent for all items classes"""

    def __init__(self, attributes: dict):
        self.__attributes = attributes if isinstance(attributes, dict) else {}

    @property
    def name(self) -> str:
        """Item name"""

        return self._get_attr('name') or ''

    @property
    def docstring(self) -> str | None:
        """Item docstring"""

        return self._get_attr('docstring')

    def _get_attr(self, attr_name: str) -> str | list | None:
        """Return attr from item's attributes or None"""

        if isinstance(attr_name, str):
            attr = self.__attributes.get(attr_name, None)
        else:
            attr = None

        return attr

    def __repr__(self) -> str:
        return str(self.name)

    def __eq__(self, item_2) -> bool:
        if isinstance(item_2, DefaultItem):
            is_equal = self.name == item_2.name
        else:
            is_equal = False

        return is_equal

    def __hash__(self) -> int:
        return hash(str(self.name))


class FunctionItem(DefaultItem):
    """Function item"""

    def is_starts_with_prefix(self, prefix: str) -> bool:
        """Check is the function starts with the prefix.

        Return True if:
        1. The function name starts with the prefix;
        2. The function name is not equal to prefix;
        3. The function name is not equal to prefix + underscore.

        """

        if isinstance(prefix, str):
            is_starts_with_prefix_ = self.name.startswith(prefix) \
                and self.name != prefix \
                and self.name != prefix + '_'
        else:
            is_starts_with_prefix_ = False

        return is_starts_with_prefix_

    @property
    def type(self) -> str | None:
        """Function type.

        All possible types described in services/code_parser.py
        in CodeParser.__get_function_type method.

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
