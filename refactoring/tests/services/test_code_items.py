"""Test services.code_items module"""

from django.test import TestCase, tag

from refactoring.services.code_items import DefaultItem
from refactoring.tests.constants import DIFFERENT_VALUES


@tag('refactoring_services', 'code_items_default_item')
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
