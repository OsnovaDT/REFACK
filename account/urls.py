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
            template_name='account/password_change/done.html',
        ),
        name='password_change_done',
    ),

    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='account/password_change/main.html',
            success_url=reverse_lazy('account:password_change_done'),
        ),
        name='password_change',
    ),

    # Password reset
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='account/password_reset/main.html',
            subject_template_name='account/password_reset/email/subject.txt',
            email_template_name='account/password_reset/email/message.html',
            success_url=reverse_lazy('account:password_reset_done'),
        ),
        name='password_reset',
    ),

    path(
        'password_reset/message_sent/',
        PasswordResetDoneView.as_view(
            template_name='account/password_reset/email/sent.html',
        ),
        name='password_reset_done',
    ),

    path(
        'password_reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='account/password_reset/confirm.html',
            success_url=reverse_lazy('account:password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),

    path(
        'password_reset/complete/',
        PasswordResetCompleteView.as_view(
            template_name='account/password_reset/done.html',
        ),
        name='password_reset_complete',
    ),
]
