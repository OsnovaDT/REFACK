"""Test urls of account app"""

from django.test import tag

from config.tests.constants import (
    ACCOUNT, LOGIN, LOGOUT, PASSWORD_CHANGE, PASSWORD_RESET, REGISTRATION,
)
from config.tests.mixins import TestURLMixin


@tag('account_urls')
class PagesTests(TestURLMixin):
    """Test pages of account app"""

    def test_login(self) -> None:
        """Test login page"""

        response = self.client.get(ACCOUNT + LOGIN)

        self.assertEqual(response.status_code, 200)

    def test_logout(self) -> None:
        """Test logout page"""

        response = self.client.get(ACCOUNT + LOGOUT)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, ACCOUNT + LOGIN)

    def test_registration(self) -> None:
        """Test registration page"""

        response = self.client.get(ACCOUNT + REGISTRATION)

        self.assertEqual(response.status_code, 200)

    def test_password_change(self) -> None:
        """Test password change page"""

        self._test_url(ACCOUNT + PASSWORD_CHANGE)
        self._test_url(ACCOUNT + PASSWORD_CHANGE, 200, True)

    def test_password_reset(self) -> None:
        """Test password reset page"""

        response = self.client.get(ACCOUNT + PASSWORD_RESET)

        self.assertEqual(response.status_code, 200)
