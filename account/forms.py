"""Forms of account app"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """User registration form"""

    class Meta:
        """Form metainformation"""

        fields = ('username', 'email', 'password1', 'password2')

        model = User
