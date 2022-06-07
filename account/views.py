"""Views of account app"""

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from account.forms import RegistrationForm


class RegistrationView(CreateView):
    """View for user registration"""

    form_class = RegistrationForm

    template_name = 'account/registration.html'

    success_url = reverse_lazy('account:login')
