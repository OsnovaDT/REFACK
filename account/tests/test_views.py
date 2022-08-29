"""Tests for account app views"""

from django.test import tag, TestCase
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from account.forms import RegistrationForm
from account.views import RegistrationView


@tag('account_views')
class RegistrationViewTests(TestCase):
    """Test RegistrationView"""

    def test_fields(self) -> None:
        """Test fields of RegistrationView"""

        self.assertEqual(
            RegistrationView.form_class,
            RegistrationForm,
        )

        self.assertEqual(
            RegistrationView.template_name,
            'account/registration.html',
        )

        self.assertEqual(
            RegistrationView.success_url,
            reverse_lazy('account:login'),
        )

    def test_mro(self) -> None:
        """Test RegistrationView MRO"""

        self.assertIn(CreateView, RegistrationView.mro())
