"""Forms of account app"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """Form for user registration"""

    email = forms.EmailField()

    class Meta:
        """Meta information about the form"""

        fields = (
            'username', 'email',
            'password1', 'password2',
        )

        model = User
