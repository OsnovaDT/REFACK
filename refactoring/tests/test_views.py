"""Tests for views of refactoring app"""

from django.test import TestCase


class ServerTests(TestCase):
    """Tests for server.py module"""

    def test_index(self):
        """Test index function"""

        response = self.client.get('/index/')

        self.assertEqual(response.status_code, 200)
