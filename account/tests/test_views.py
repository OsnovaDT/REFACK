"""Test views of account app"""

from django.test import TestCase, tag
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from account.forms import RegistrationForm
from account.views import RegistrationView


@tag('account_views')
class RegistrationViewTests(TestCase):
    """Test RegistrationView of account app"""

    def test_registration_view(self) -> None:
        """Test RegistrationView"""

        self.assertEqual(
            RegistrationView.form_class, RegistrationForm,
        )

        self.assertEqual(
            RegistrationView.template_name, 'account/registration.html',
        )

        self.assertEqual(
            RegistrationView.success_url, reverse_lazy('account:login'),
        )

    def test_create_view_in_mro(self) -> None:
        """Test that CreateView in RegistrationView MRO"""

        self.assertIn(CreateView, RegistrationView.mro())
