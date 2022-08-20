"""Test services.code_items module"""

from django.test import TestCase, tag

from refactoring.services.code_items import (
    DefaultItem, FunctionItem, ClassItem,
)
from refactoring.tests.constants import (
    DIFFERENT_VALUES, NOT_STRING_VALUES, INCORRECT_GET_NAMES,
    CORRECT_GET_NAMES, INCORRECT_BOOL_NAMES, CORRECT_BOOL_NAMES,
)


@tag('refactoring_services', 'refactoring_services_code_items')
class DefaultItemTests(TestCase):
    """Test DefaultItem class"""

    def setUp(self) -> None:
        self.test_name_1 = 'test name'

        self.test_docstring_1 = 'test docstring 1'
        self.test_docstring_2 = 'test docstring 2'

        self.default_item_1 = DefaultItem({
            'name': self.test_name_1,
            'docstring': self.test_docstring_1,
        })

        self.default_item_2 = DefaultItem({
            'name': self.test_name_1,
            'docstring': self.test_docstring_2,
        })

        self.none_default_item = DefaultItem({
            'name': None,
            'docstring': None,
        })

        self.empty_default_item = DefaultItem('test string')

    def test_name(self) -> None:
        """Test name property"""

        self.assertEqual(self.default_item_1.name, self.test_name_1)
        self.assertEqual(self.none_default_item.name, '')
        self.assertEqual(self.empty_default_item.name, '')

    def test_docstring(self) -> None:
        """Test docstring property"""

        self.assertEqual(
            self.default_item_1.docstring,
            self.test_docstring_1,
        )

        self.assertEqual(self.none_default_item.docstring, None)
        self.assertEqual(self.empty_default_item.docstring, None)

    def test_repr(self) -> None:
        """Test __repr__ method"""

        self.assertEqual(str(self.default_item_1), self.test_name_1)
        self.assertEqual(str(self.none_default_item), '')

    def test_eq(self) -> None:
        """Test __eq__ method"""

        self.assertTrue(self.default_item_1 == self.default_item_2)

        for value in DIFFERENT_VALUES:
            self.assertFalse(self.default_item_1 == value)

    def test_hash(self) -> None:
        """Test __hash__ method"""

        self.assertEqual(
            hash(self.default_item_1),
            hash(str(self.test_name_1)),
        )

        self.assertEqual(
            hash(self.none_default_item),
            hash(''),
        )

    def test_get_attr(self) -> None:
        """Test _get_attr method"""

        self.assertEqual(
            self.default_item_1._get_attr('name'),
            self.test_name_1,
        )

        self.assertEqual(
            self.default_item_1._get_attr('docstring'),
            self.test_docstring_1,
        )

        for value in DIFFERENT_VALUES:
            self.assertEqual(self.default_item_1._get_attr(value), None)


@tag('refactoring_services', 'refactoring_services_code_items')
class FunctionItemTests(TestCase):
    """Test FunctionItem class"""

    def setUp(self) -> None:
        self.test_data_1 = {
            'name': 'is_correct',
            'docstring': 'test docstring 1',
        }

        self.test_data_2 = {
            'name': 'get_value',
            'type': 'not bool',
            'docstring': 'test docstring 2',
            'type_hint': 'str',
        }

        self.test_data_3 = {
            'name': 'get_value',
            'type': 'pass',
            'docstring': 'test docstring 2',
            'type_hint': 'str',
            'args': ['arg1', 'arg2'],
        }

        self.function_item_1 = FunctionItem(self.test_data_1)
        self.function_item_2 = FunctionItem(self.test_data_2)
        self.function_item_3 = FunctionItem(self.test_data_3)

    def test_inherits_from_default_item(self) -> None:
        """Test that class inherit from DefaultItem"""

        self.assertIn(DefaultItem, FunctionItem.mro())

    def test_type(self) -> None:
        """Test type property"""

        self.assertEqual(self.function_item_1.type, None)
        self.assertEqual(self.function_item_2.type, self.test_data_2['type'])
        self.assertEqual(self.function_item_3.type, self.test_data_3['type'])

    def test_type_hint(self) -> None:
        """Test type_hint property"""

        self.assertEqual(self.function_item_1.type_hint, None)

        self.assertEqual(
            self.function_item_2.type_hint,
            self.test_data_2['type_hint'],
        )

        self.assertEqual(
            self.function_item_3.type_hint,
            self.test_data_3['type_hint'],
        )

    def test_args(self) -> None:
        """Test args property"""

        self.assertEqual(self.function_item_1.args, None)
        self.assertEqual(self.function_item_2.args, None)
        self.assertEqual(self.function_item_3.args, self.test_data_3['args'])

    def test_is_start_with_prefix_get_(self) -> None:
        """Test is_start_with_prefix_get_ function"""

        for name in INCORRECT_GET_NAMES:
            with self.subTest(f'{name=}'):
                self.assertFalse(
                    FunctionItem({'name': name}).is_start_with_prefix_get_()
                )

        for name in CORRECT_GET_NAMES:
            with self.subTest(f'{name=}'):
                self.assertTrue(
                    FunctionItem({'name': name}).is_start_with_prefix_get_()
                )

    def test_is_start_with_prefix_is_(self) -> None:
        """Test is_start_with_prefix_is_ function"""

        for name in INCORRECT_BOOL_NAMES:
            with self.subTest(f'{name=}'):
                self.assertFalse(
                    FunctionItem({'name': name}).is_start_with_prefix_is_()
                )

        for name in CORRECT_BOOL_NAMES:
            with self.subTest(f'{name=}'):
                self.assertTrue(
                    FunctionItem({'name': name}).is_start_with_prefix_is_()
                )

    def test_is_start_with_prefix(self):
        """Test __is_start_with_prefix function"""

        self.assertFalse(
            FunctionItem({
                'name': 'is_'
            })._FunctionItem__is_start_with_prefix('is_')
        )

        self.assertFalse(
            FunctionItem({
                'name': 'get_'
            })._FunctionItem__is_start_with_prefix('get_')
        )

        self.assertFalse(
            FunctionItem({
                'name': 'setValue'
            })._FunctionItem__is_start_with_prefix('is_')
        )

        self.assertFalse(
            FunctionItem({
                'name': 'getValue'
            })._FunctionItem__is_start_with_prefix('get_')
        )

        self.assertTrue(
            FunctionItem({
                'name': 'get_value'
            })._FunctionItem__is_start_with_prefix('get_')
        )

        self.assertTrue(
            FunctionItem({
                'name': 'is_correct'
            })._FunctionItem__is_start_with_prefix('is_')
        )

        for value in NOT_STRING_VALUES:
            self.assertFalse(
                FunctionItem({
                    'name': 'set_name'
                })._FunctionItem__is_start_with_prefix(value)
            )


@tag('refactoring_services', 'refactoring_services_code_items')
class ClassItemTests(TestCase):
    """Test ClassItem class"""

    def test_inherits_from_default_item(self) -> None:
        """Test that class inherit from DefaultItem"""

        self.assertIn(DefaultItem, ClassItem.mro())
