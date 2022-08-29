"""Tests for account app apps"""

from django.test import tag, TestCase

from account.apps import AccountConfig
from config.tests.constants import DEFAULT_AUTO_FIELD


@tag("account_config")
class AccountConfigTests(TestCase):
    """Test AccountConfig class"""

    def test_default_auto_field(self) -> None:
        """Test default_auto_field attr"""

        self.assertEqual(
            AccountConfig.default_auto_field,
            DEFAULT_AUTO_FIELD,
        )

    def test_name(self) -> None:
        """Test name attr"""

        self.assertEqual(
            AccountConfig.name,
            "account",
        )
