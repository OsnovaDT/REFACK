"""Test forms of account app"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import TestCase, tag

from account.forms import RegistrationForm


@tag('account_forms')
class RegistrationFormTests(TestCase):
    """Test RegistrationForm of account app"""

    def test_form_fields(self) -> None:
        """Test fields attribute"""

        self.assertEqual(
            RegistrationForm._meta.fields,
            ('username', 'email', 'password1', 'password2',),
        )

    def test_form_model(self) -> None:
        """Test model attribute"""

        self.assertEqual(RegistrationForm._meta.model, User)

    def test_user_creation_form_in_mro(self) -> None:
        """Test that UserCreationForm in RegistrationForm MRO"""

        self.assertIn(UserCreationForm, RegistrationForm.mro())
