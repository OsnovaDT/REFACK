"""Tests for views of refactoring app"""

from django.test import TestCase


class PagesTests(TestCase):
    """Tests for refactoring's pages"""

    def test_index(self) -> None:
        """Test index page"""

        response = self.client.get('')

        self.assertEqual(response.status_code, 200)

    def test_manual_input(self) -> None:
        """Test manual input page"""

        response = self.client.get('/manual_input/')

        self.assertEqual(response.status_code, 200)

    def test_instruction(self) -> None:
        """Test instruction page"""

        response = self.client.get('/instruction/')

        self.assertEqual(response.status_code, 200)

    def test_rules(self) -> None:
        """Test rules page"""

        response = self.client.get('/rules/')

        self.assertEqual(response.status_code, 200)
