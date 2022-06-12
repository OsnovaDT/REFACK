"""Nodes for user's modules"""


class DefaltNode:
    """Default node that contain info about user's modules"""

    def __init__(self, info: dict):
        self.__info = info

    def _get_attr_from_info(self, attr_name: str) -> str | None:
        """Look for attribute in function info and return it or None"""

        if attr_name in self.__info.keys():
            attr = self.__info[attr_name]
        else:
            attr = None

        return attr

    @property
    def name(self) -> str | None:
        """Name property"""

        return self._get_attr_from_info('name')

    @property
    def docstring(self) -> str | None:
        """Docstring property"""

        return self._get_attr_from_info('docstring')


class FunctionNode(DefaltNode):
    """Contain all info about function from user's code"""

    @property
    def type(self) -> str | None:
        """Type property"""

        return self._get_attr_from_info('type')

    @property
    def type_annotation(self) -> str | None:
        """Type annotation that specified after function definition.

        For example for this function:

        def get_name() -> str:
            pass

        type annotations will be str

        """

        return self._get_attr_from_info('type_annotation')


class ClassNode(DefaltNode):
    """Contain all info about class from user's code"""
