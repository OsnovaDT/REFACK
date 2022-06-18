"""Urls of account app"""

from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, reverse_lazy

from account.views import RegistrationView


app_name = 'account'

urlpatterns = [
    # Login and logout
    path(
        'login/',
        LoginView.as_view(
            template_name='account/login.html',
        ),
        name='login',
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout',
    ),

    # Registration
    path(
        'registration/',
        RegistrationView.as_view(),
        name='registration',
    ),

    # Password change
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='account/password_changed.html',
        ),
        name='password_change_done',
    ),

    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='account/password_change.html',
            success_url=reverse_lazy('account:password_change_done'),
        ),
        name='password_change',
    ),

    # Password reset
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='account/password_reset/password_reset.html',
            subject_template_name='account/password_reset/email_subject.txt',
            email_template_name='account/password_reset/email_message.html',
            success_url=reverse_lazy('account:password_reset_done'),
        ),
        name='password_reset',
    ),

    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='account/password_reset/email_sent.html',
        ),
        name='password_reset_done',
    ),

    path(
        'password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='account/password_reset/password_reset_confirm.html',
            success_url=reverse_lazy('account:password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),

    path(
        'password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name='account/password_reset/'
            'password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]
