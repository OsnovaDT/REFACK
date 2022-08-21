"""Test services.code_parser module"""

from ast import parse, Return, Constant

from django.test import TestCase, tag

from refactoring.services.code_parser import CodeParser
from refactoring.tests.constants import (
    CODE_WITH_FUNCTIONS, FUNCTION_ITEMS, CODE_WITH_CLASSES, CLASS_ITEMS,
    BOOL_TYPE, NOT_BOOL_TYPE, DIFFERENT_VALUES,
)


@tag('refactoring_services', 'refactoring_services_code_parser')
class CodeParserTests(TestCase):
    """Test CodeParser class"""

    def setUp(self) -> None:
        self.code_parser = CodeParser()
        self.code_parser_items = self.code_parser._CodeParser__code_items

    def test_visit_FunctionDef(self) -> None:
        """Test visit_FunctionDef method"""

        self.assertEqual(dict(self.code_parser_items), {})

        parsed_functions = parse(CODE_WITH_FUNCTIONS).__dict__['body']

        for func in parsed_functions:
            self.code_parser.visit_FunctionDef(func)

        for value in DIFFERENT_VALUES:
            self.code_parser.visit_FunctionDef(value)

        for index in range(len(parsed_functions)):
            real_code_item = list(dict(self.code_parser_items)[
                'functions'
            ][index].__dict__.values())[0]

            if real_code_item['type_hint']:
                real_code_item['type_hint'] = real_code_item['type_hint'].id

            for i in range(len(real_code_item['args'])):
                arg_name = real_code_item['args'][i].arg
                arg_type_hint = ''

                if real_code_item['args'][i].annotation:
                    arg_type_hint = real_code_item['args'][i].annotation.id
                real_code_item['args'][i] = f'{arg_name}: {arg_type_hint}'

            self.assertEqual(real_code_item, FUNCTION_ITEMS[index])

    def test_visit_ClassDef(self) -> None:
        """Test visit_ClassDef method"""

        self.assertEqual(dict(self.code_parser_items), {})

        parsed_classes = parse(CODE_WITH_CLASSES).__dict__['body']

        for class_ in parsed_classes:
            self.code_parser.visit_ClassDef(class_)

        for value in DIFFERENT_VALUES:
            self.code_parser.visit_ClassDef(value)

        for index in range(len(parsed_classes)):
            self.assertEqual(
                dict(self.code_parser_items)['classes'][index].__dict__,
                CLASS_ITEMS[index].__dict__,
            )

    def test_code_items_property(self) -> None:
        """Test code_items property"""

        self.assertEqual(self.code_parser.code_items, {})

        for func in parse(CODE_WITH_FUNCTIONS).__dict__['body']:
            self.code_parser.visit_FunctionDef(func)

        for class_ in parse(CODE_WITH_CLASSES).__dict__['body']:
            self.code_parser.visit_ClassDef(class_)

        self.assertNotEqual(len(self.code_parser.code_items), 0)
        self.assertEqual(self.code_parser.code_items, self.code_parser_items)

    def test_get_type_of_return(self) -> None:
        """Test __get_type_of_return method"""

        true_return = Return(value=Constant(value=True))
        false_return = Return(value=Constant(value=False))

        for bool_return in [true_return, false_return]:
            self.assertEqual(
                self.code_parser._CodeParser__get_type_of_return(bool_return),
                BOOL_TYPE,
            )

        int_return = Return(value=Constant(value=100))
        str_return = Return(value=Constant(value='test string'))
        bytes_return = Return(value=Constant(value=b'test string'))
        float_return = Return(value=Constant(value=10.11))

        for return_ in [int_return, str_return, bytes_return, float_return]:
            self.assertEqual(
                self.code_parser._CodeParser__get_type_of_return(return_),
                NOT_BOOL_TYPE,
            )

        for value in DIFFERENT_VALUES:
            self.assertEqual(
                self.code_parser._CodeParser__get_type_of_return(value),
                NOT_BOOL_TYPE,
            )
