"""Tests for views of account app"""

from django.contrib.auth import get_user_model
from django.test import TestCase, tag

from account.tests.constants import (
    ACCOUNT, LOGIN, LOGOUT, PASSWORD_CHANGE, PASSWORD_RESET, REGISTRATION,
    SUPERUSER_USERNAME, SUPERUSER_PASSWORD,
)


User = get_user_model()


@tag('account_urls')
class PagesTests(TestCase):
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

        response = self.client.get(ACCOUNT + PASSWORD_CHANGE)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            ACCOUNT + LOGIN + '?next=' + ACCOUNT + PASSWORD_CHANGE,
        )

        User.objects.create_superuser(
            username=SUPERUSER_USERNAME, password=SUPERUSER_PASSWORD,
        )

        self.client.post(
            ACCOUNT + LOGIN,
            {
                'username': SUPERUSER_USERNAME,
                'password': SUPERUSER_PASSWORD,
            },
        )

        response = self.client.get(ACCOUNT + PASSWORD_CHANGE)

        self.assertEqual(response.status_code, 200)

    def test_password_reset(self) -> None:
        """Test password reset page"""

        response = self.client.get(ACCOUNT + PASSWORD_RESET)

        self.assertEqual(response.status_code, 200)
