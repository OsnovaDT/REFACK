"""Tests for views of account app"""

from django.test import TestCase


class PagesTests(TestCase):
    """Tests for pages of account app"""

    __ACCOUNT_URL = '/account/'

    def test_login(self) -> None:
        """Test login page"""

        response = self.client.get(self.__ACCOUNT_URL + 'login/')

        self.assertEqual(response.status_code, 200)

    def test_logout(self) -> None:
        """Test logout page"""

        response = self.client.get(self.__ACCOUNT_URL + 'logout/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.__ACCOUNT_URL + 'login/')

    def test_password_change(self) -> None:
        """Test password change page"""

        response = self.client.get(self.__ACCOUNT_URL + 'password_change/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            self.__ACCOUNT_URL + 'login/?next=' +
            self.__ACCOUNT_URL + 'password_change/'
        )

    def test_password_reset(self) -> None:
        """Test password reset page"""

        response = self.client.get(self.__ACCOUNT_URL + 'password_reset/')

        self.assertEqual(response.status_code, 200)

    def test_registration(self) -> None:
        """Test registration page"""

        response = self.client.get(self.__ACCOUNT_URL + 'registration/')

        self.assertEqual(response.status_code, 200)
