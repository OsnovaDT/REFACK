"""Tests for views of account app"""

from django.test import TestCase


class PagesTests(TestCase):
    """Tests for account's pages"""

    def test_login(self):
        """Test index page"""

        response = self.client.get('/account/login/')

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Test logout page"""

        response = self.client.get('/account/logout/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/account/login/')

    def test_password_change(self):
        """Test password change page"""

        response = self.client.get('/account/password_change/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            '/account/login/?next=/account/password_change/'
        )

    def test_password_reset(self):
        """Test password reset page"""

        response = self.client.get('/account/password_reset/')

        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        """Test registration page"""

        response = self.client.get('/account/registration/')

        self.assertEqual(response.status_code, 200)
