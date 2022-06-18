"""Forms of account app"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """User registration form"""

    email = forms.EmailField()

    class Meta:
        """RegistrationForm info"""

        fields = ('username', 'email', 'password1', 'password2',)

        model = User
