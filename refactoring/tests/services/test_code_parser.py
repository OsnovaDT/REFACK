"""Test services.code_parser module"""

from ast import parse

from django.test import TestCase, tag

from refactoring.services.code_parser import CodeParser
from refactoring.tests.constants import (
    CODE_WITH_FUNCTIONS, FUNCTION_ITEMS, CODE_WITH_CLASSES, CLASS_ITEMS,
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
