"""Tests for views of refactoring app"""

from django.test import TestCase


class PagesTests(TestCase):
    """Tests for refactoring's pages"""

    def test_index(self) -> None:
        """Test index page"""

        response = self.client.get('')

        self.assertEqual(response.status_code, 200)

    def test_code_input(self) -> None:
        """Test code input page"""

        response = self.client.get('/code_input/')

        self.assertEqual(response.status_code, 200)

    def test_rules(self) -> None:
        """Test rules page"""

        response = self.client.get('/rules/')

        self.assertEqual(response.status_code, 200)
