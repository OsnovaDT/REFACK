"""Tests for account app forms"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import tag, TestCase

from account.forms import RegistrationForm


@tag('account_forms')
class RegistrationFormTests(TestCase):
    """Test RegistrationForm"""

    def test_fields_attr(self) -> None:
        """Test fields attr from metainformation"""

        self.assertEqual(
            RegistrationForm._meta.fields,
            ('username', 'email', 'password1', 'password2'),
        )

    def test_model_attr(self) -> None:
        """Test model attr from metainformation"""

        self.assertEqual(RegistrationForm._meta.model, User)

    def test_mro(self) -> None:
        """Test RegistrationForm MRO"""

        self.assertIn(UserCreationForm, RegistrationForm.mro())
