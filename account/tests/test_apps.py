"""Test config of account app"""

from django.test import TestCase, tag

from account.apps import AccountConfig
from config.tests.constants import DEFAULT_AUTO_FIELD


@tag('account_config')
class AccountConfigTests(TestCase):
    """Test AccountConfig class"""

    def test_default_auto_field(self) -> None:
        """Test default_auto_field attribute"""

        self.assertEqual(
            AccountConfig.default_auto_field, DEFAULT_AUTO_FIELD,
        )

    def test_name(self) -> None:
        """Test name attribute"""

        self.assertEqual(AccountConfig.name, 'account')
